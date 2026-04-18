from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Student, Faculty, Course


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid Credentials'})

    return render(request, 'login.html')


def home(request):
    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})


def add_student(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        course = request.POST.get("course")

        Student.objects.create(name=name, age=age, course=course)
        return redirect('home')

    return render(request, 'add_student.html')


def add_faculty(request):
    if request.method == "POST":
        name = request.POST.get("name")
        subject = request.POST.get("subject")

        Faculty.objects.create(name=name, subject=subject)
        return redirect('home')

    return render(request, 'add_faculty.html')


def add_course(request):
    if request.method == "POST":
        name = request.POST.get("name")

        Course.objects.create(name=name)
        return redirect('home')

    return render(request, 'add_course.html')


def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('home')


def logout_view(request):
    logout(request)
    return redirect('login')