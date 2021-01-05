from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=50, null=True)
    num_e = models.IntegerField(null=True)
    num_m = models.IntegerField(null=True)
    num_b = models.IntegerField(null=True)
    feed = models.CharField(max_length=100, null=True)
    number = models.CharField(max_length=11, null=True)
    manager = models.ForeignKey(User, on_delete = models.CASCADE)
    

    def __str__(self):
        return self.name
    
