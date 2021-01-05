from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.students,name='students' ),
    path('add/', views.add, name='add'),
    path('edit/<int:pk>/', views.edit, name='edit'), 
    path('delete/<int:pk>/', views.delete, name='delete') 
]