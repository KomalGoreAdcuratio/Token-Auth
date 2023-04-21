from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=25)
    owner = models.ForeignKey('auth.User', related_name='students', on_delete=models.CASCADE)
    highlighted = models.TextField()
