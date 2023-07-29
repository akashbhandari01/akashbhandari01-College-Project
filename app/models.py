
from django.db import models
from django.contrib import admin
from django.urls import *

class Contact(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    universityroll=models.IntegerField()
    message=models.TextField()
    def __str__(self):
        return self.name
    
