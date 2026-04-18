from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('home/', views.home, name='home'),

    path('add/', views.add_student, name='add_student'),
    path('addfaculty/', views.add_faculty, name='add_faculty'),
    path('addcourse/', views.add_course, name='add_course'),

    path('delete/<int:id>/', views.delete_student, name='delete_student'),
    path('logout/', views.logout_view, name='logout'),
]