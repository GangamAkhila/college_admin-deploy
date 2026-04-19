from django.contrib import admin
from .models import Department, Course, Faculty, Student, Notice

admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Faculty)
admin.site.register(Student)
admin.site.register(Notice)
