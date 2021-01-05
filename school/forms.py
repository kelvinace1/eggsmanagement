from django import forms 
from .models import *
from django.forms import ModelForm

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student 
        fields = ['name', 'address', 'num_e', 'num_m', 'num_b', 'feed', 'number']