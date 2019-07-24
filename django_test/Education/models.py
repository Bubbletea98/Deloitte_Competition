from django.db import models
from django.utils import timezone
from datetime import timedelta  
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content =models.TextField()
    date_posted=models.DateTimeField(default=timezone.now())
    Teacher = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__ (self):
        return self.title

class School(models.Model):
	name = models.CharField(max_length=100)
	latitude = models.IntegerField()
	longitude = models.IntegerField()

class Person(models.Model):
	name = models.CharField(max_length=100)
	school = models.ForeignKey(School, on_delete=models.CASCADE)

class Class(models.Model):
	name = models.CharField(max_length=100)
	school = models.ForeignKey(School, on_delete=models.CASCADE)

class Student(Person):
	class_name = models.ForeignKey(Class, on_delete=models.CASCADE)

class Learning(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)

class MovableResource(models.Model):
	name = models.CharField(max_length=100)
	availableStart = models.DateTimeField(default=timezone.now())
	availableEnd = models.DateTimeField(default=timezone.now() + timedelta(days=1) )
