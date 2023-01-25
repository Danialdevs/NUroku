from django.db import models
from django.contrib.auth.models import User
from datetime import time
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class Role(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class School(models.Model):
  name = models.CharField(max_length=255)
  general= models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
  def __str__(self):
        return self.name
    
class Subject(models.Model):
    name = models.CharField(max_length=255)
    school = models.ForeignKey(School, on_delete=models.CASCADE,null=True, blank=True)
    def __str__(self):
      return self.name
      

class Teacher(models.Model):
   name = models.CharField(max_length=255)
   subjects = models.ManyToManyField(Subject)
   email = models.EmailField()
   role = models.ForeignKey(Role, on_delete=models.CASCADE, default=1)
   user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
   subjects = models.ManyToManyField(Subject)
   def __str__(self):
       return self.name

class Class(models.Model):
  school = models.ForeignKey(School, on_delete=models.CASCADE)
  letter = models.CharField(max_length=5)
  number = models.IntegerField()
  Teacher = models.ManyToManyField(Teacher)


class Access(models.Model):
  school = models.ForeignKey(School, on_delete=models.CASCADE)
  subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
  teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
  Class = models.ForeignKey(Class, on_delete=models.CASCADE)
      
class Schedule(models.Model):
    DAY_OF_WEEK_CHOICES = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    )
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=9, choices=DAY_OF_WEEK_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField(default=time.max)

class Student(models.Model): 
  Class = models.ForeignKey(Class, on_delete=models.CASCADE)
  school = models.ForeignKey(School, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)

class Mark(models.Model):
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
  teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
  date = models.DateField()
  mark = models.CharField(max_length=2)
  comment = models.TextField(blank=True)

class Book(models.Model):
  Name = models.CharField(max_length=50)
  Class = models.IntegerField()
  File = models.FileField(upload_to=None, max_length=254)

class News(models.Model):
  Title = models.CharField(max_length=50)
  Text = models.TextField()

