# app1/models.py
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Faculty(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    course = models.CharField(max_length=50)

    def __str__(self):
        return self.name