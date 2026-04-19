from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    # Auth
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    
    # Dashboard & API
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('api/stats/', views.api_stats, name='api_stats'),

    # Departments
    path('departments/', views.DepartmentListView.as_view(), name='department_list'),
    path('departments/add/', views.DepartmentCreateView.as_view(), name='department_add'),
    path('departments/<int:pk>/edit/', views.DepartmentUpdateView.as_view(), name='department_edit'),
    path('departments/<int:pk>/delete/', views.DepartmentDeleteView.as_view(), name='department_delete'),

    # Courses
    path('courses/', views.CourseListView.as_view(), name='course_list'),
    path('courses/add/', views.CourseCreateView.as_view(), name='course_add'),
    path('courses/<int:pk>/edit/', views.CourseUpdateView.as_view(), name='course_edit'),
    path('courses/<int:pk>/delete/', views.CourseDeleteView.as_view(), name='course_delete'),

    # Faculty
    path('faculty/', views.FacultyListView.as_view(), name='faculty_list'),
    path('faculty/add/', views.FacultyCreateView.as_view(), name='faculty_add'),
    path('faculty/<int:pk>/edit/', views.FacultyUpdateView.as_view(), name='faculty_edit'),
    path('faculty/<int:pk>/delete/', views.FacultyDeleteView.as_view(), name='faculty_delete'),

    # Students
    path('students/', views.StudentListView.as_view(), name='student_list'),
    path('students/add/', views.StudentCreateView.as_view(), name='student_add'),
    path('students/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('students/<int:pk>/edit/', views.StudentUpdateView.as_view(), name='student_edit'),
    path('students/<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student_delete'),

    # Notices
    path('notices/', views.NoticeListView.as_view(), name='notice_list'),
    path('notices/add/', views.NoticeCreateView.as_view(), name='notice_add'),
    path('notices/<int:pk>/edit/', views.NoticeUpdateView.as_view(), name='notice_edit'),
    path('notices/<int:pk>/delete/', views.NoticeDeleteView.as_view(), name='notice_delete'),
]