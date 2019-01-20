from django.urls import path

from . import views

urlpatterns = [
    path('students/', views.ListStudent.as_view()),
    path('students/<int:pk>/', views.DetailStudent.as_view()),
    path('schools/', views.ListSchool.as_view()),
    path('schools/<int:pk>/', views.DetailSchool.as_view()),
]