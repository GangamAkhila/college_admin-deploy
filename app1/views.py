from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from .models import Department, Course, Faculty, Student, Notice
from .forms import DepartmentForm, CourseForm, FacultyForm, StudentForm, NoticeForm

class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student_count'] = Student.objects.count()
        context['faculty_count'] = Faculty.objects.count()
        context['course_count'] = Course.objects.count()
        context['department_count'] = Department.objects.count()
        context['recent_notices'] = Notice.objects.order_by('-created_at')[:5]
        context['recent_students'] = Student.objects.order_by('-id')[:5]
        return context

def api_stats(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Unauthorized'}, status=401)
    
    data = {
        'students': Student.objects.count(),
        'faculty': Faculty.objects.count(),
        'courses': Course.objects.count(),
        'departments': Department.objects.count(),
    }
    return JsonResponse(data)

# Mixins for common behavior
class BaseListView(LoginRequiredMixin, ListView):
    paginate_by = 10

class BaseCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    def form_invalid(self, form):
        messages.error(self.request, "Please correct the errors below.")
        return super().form_invalid(form)

class BaseUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    def form_invalid(self, form):
        messages.error(self.request, "Please correct the errors below.")
        return super().form_invalid(form)

class BaseDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'confirm_delete.html'
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, f"{self.model.__name__} deleted successfully.")
        return super().delete(request, *args, **kwargs)

# Departments
class DepartmentListView(BaseListView):
    model = Department
    template_name = 'departments/list.html'
    context_object_name = 'departments'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Department.objects.filter(Q(name__icontains=query) | Q(code__icontains=query))
        return Department.objects.all()

class DepartmentCreateView(BaseCreateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'departments/form.html'
    success_url = reverse_lazy('department_list')
    success_message = "Department created successfully!"

class DepartmentUpdateView(BaseUpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'departments/form.html'
    success_url = reverse_lazy('department_list')
    success_message = "Department updated successfully!"

class DepartmentDeleteView(BaseDeleteView):
    model = Department
    success_url = reverse_lazy('department_list')

# Courses
class CourseListView(BaseListView):
    model = Course
    template_name = 'courses/list.html'
    context_object_name = 'courses'

    def get_queryset(self):
        query = self.request.GET.get('q')
        qs = Course.objects.select_related('department')
        if query:
            qs = qs.filter(Q(name__icontains=query) | Q(code__icontains=query))
        return qs

class CourseCreateView(BaseCreateView):
    model = Course
    form_class = CourseForm
    template_name = 'courses/form.html'
    success_url = reverse_lazy('course_list')
    success_message = "Course created successfully!"

class CourseUpdateView(BaseUpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'courses/form.html'
    success_url = reverse_lazy('course_list')
    success_message = "Course updated successfully!"

class CourseDeleteView(BaseDeleteView):
    model = Course
    success_url = reverse_lazy('course_list')

# Faculty
class FacultyListView(BaseListView):
    model = Faculty
    template_name = 'faculty/list.html'
    context_object_name = 'faculties'

    def get_queryset(self):
        query = self.request.GET.get('q')
        qs = Faculty.objects.select_related('department')
        if query:
            qs = qs.filter(Q(name__icontains=query) | Q(employee_id__icontains=query))
        return qs

class FacultyCreateView(BaseCreateView):
    model = Faculty
    form_class = FacultyForm
    template_name = 'faculty/form.html'
    success_url = reverse_lazy('faculty_list')
    success_message = "Faculty member added successfully!"

class FacultyUpdateView(BaseUpdateView):
    model = Faculty
    form_class = FacultyForm
    template_name = 'faculty/form.html'
    success_url = reverse_lazy('faculty_list')
    success_message = "Faculty details updated successfully!"

class FacultyDeleteView(BaseDeleteView):
    model = Faculty
    success_url = reverse_lazy('faculty_list')

# Students
class StudentListView(BaseListView):
    model = Student
    template_name = 'students/list.html'
    context_object_name = 'students'

    def get_queryset(self):
        query = self.request.GET.get('q')
        qs = Student.objects.select_related('course')
        if query:
            qs = qs.filter(Q(name__icontains=query) | Q(roll_number__icontains=query))
        return qs

class StudentCreateView(BaseCreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/form.html'
    success_url = reverse_lazy('student_list')
    success_message = "Student admitted successfully!"

class StudentUpdateView(BaseUpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/form.html'
    success_url = reverse_lazy('student_list')
    success_message = "Student details updated successfully!"

class StudentDeleteView(BaseDeleteView):
    model = Student
    success_url = reverse_lazy('student_list')

class StudentDetailView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = 'students/detail.html'
    context_object_name = 'student'

# Notices
class NoticeListView(BaseListView):
    model = Notice
    template_name = 'notices/list.html'
    context_object_name = 'notices'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        qs = Notice.objects.all()
        if query:
            qs = qs.filter(title__icontains=query)
        return qs

class NoticeCreateView(BaseCreateView):
    model = Notice
    form_class = NoticeForm
    template_name = 'notices/form.html'
    success_url = reverse_lazy('notice_list')
    success_message = "Notice posted successfully!"

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)

class NoticeUpdateView(BaseUpdateView):
    model = Notice
    form_class = NoticeForm
    template_name = 'notices/form.html'
    success_url = reverse_lazy('notice_list')
    success_message = "Notice updated successfully!"

class NoticeDeleteView(BaseDeleteView):
    model = Notice
    success_url = reverse_lazy('notice_list')