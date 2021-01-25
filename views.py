from django.shortcuts import render, redirect
from .models import Student
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

# Create your views here.
def home(request):
    return render(request, "school/home.html")


class CustomerView(ListView):
    model = Student 
    template_name = 'school/customers.html'
    context_object_name = 'students'
    
class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student 
    fields = ['name', 'address', 'amount', 'balance', 'number']

    def form_valid(self, form):
        form.instance.manager = self.request.user  
        return super().form_valid(form)


class StudentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Student 
    fields = ['name', 'address',  'amount', 'balance', 'number']

    def form_valid(self, form):
        form.instance.manager = self.request.user  
        return super().form_valid(form)

    def test_func(self):
        student = self.get_object()
        if self.request.user == student.manager:
            return True
        return False

class StudentDetailView(DetailView):
    model = Student


class StudentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Student 
    success_url = '/'

    def form_valid(self, form):
        form.instance.manager = self.request.user  
        return super().form_valid(form)

    def test_func(self):
        student = self.get_object()
        if self.request.user == student.manager:
            return True
        return False

    

