from django.shortcuts import render, redirect
from .models import Student
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    
    return render(request, "school/home.html")

def students(request):
    user = request.user 
    context = {
        'students':Student.objects.all()
    }
    return render(request, "school/students.html", context)
  


@login_required
def add(request):
     if request.method == "POST":
        form = StudentForm(request.POST)
        
        if form.is_valid():
            form.save()
        return redirect('/students')
     else:
        form = StudentForm()
     form = StudentForm()
     students = Student.objects.all()
     context = {'students':students,'form':form }
     return render(request, "school/add_students.html", context)


def edit(request, pk):
    student = Student.objects.get(id=pk)
    form = StudentForm(instance=student)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
        return redirect('/students')
        
    context = {
        'form':form
    }
    return render(request, "school/update.html", context)

def delete(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == "POST":
        student.delete()
        return redirect('/students')
    

    context = {
        'student':student
    }

    return render(request, "school/delete.html", context)
    

