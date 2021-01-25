from django.urls import path 
from . import views 
from .views import  StudentDeleteView, StudentCreateView, StudentUpdateView, CustomerView, StudentDetailView

urlpatterns = [
    path('',views.home, name='home'),
    path('customers/', CustomerView.as_view(),name='student-list' ),
    path('student/new', StudentCreateView.as_view(), name='student-create'),
    path('student/<int:pk>/update', StudentUpdateView.as_view(), name='student-update'), 
    path('student/<int:pk>/delete/', StudentDeleteView.as_view(), name='student-delete'),
    path('student/<int:pk>/', StudentDetailView.as_view(), name='student-detail')
]