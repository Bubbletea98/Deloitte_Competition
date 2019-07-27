from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content =models.TextField()
    date_posted=models.DateTimeField(default=timezone.now())
    Teacher = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__ (self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk': self.pk})


class School(models.Model):
	name = models.CharField(max_length=100)
	latitude = models.FloatField(default=116.391467)
	longitude = models.FloatField(default=39.927761)
	address = models.CharField(max_length=100, default='')

class Person(models.Model):
	name = models.CharField(max_length=100)
	school = models.ForeignKey(School, on_delete=models.CASCADE,)


class Class(models.Model):
	name = models.CharField(max_length=100)
	school = models.ForeignKey(School, on_delete=models.CASCADE)

class Teacher(Person):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
	class_name = models.OneToOneField(Class, on_delete=models.CASCADE, null=True)
	image = models.ImageField(default='default.jpg',upload_to='profile_pics')

class Student(Person):
	class_name = models.ForeignKey(Class, on_delete=models.CASCADE)

class LearningType(models.Model):
	name = models.CharField(max_length=100, default='')

# Class manage the learning status for a given area of study of a student
class Learning(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	ability = models.IntegerField(default=0)
	estimation = models.FloatField(default=0)
	MaxAbility = models.IntegerField(default=10)
	learningType = models.ForeignKey(LearningType, on_delete=models.CASCADE, null=True)

class Problem(models.Model):
	difficulty = models.IntegerField()
	isCorrect = models.BooleanField()
	learning = models.ForeignKey(Learning, on_delete=models.CASCADE, related_name='problems')

class MovableResource(models.Model):
	name = models.CharField(max_length=100)
	availableStart = models.DateTimeField(default=timezone.now())
	availableEnd = models.DateTimeField(default=timezone.now() + timedelta(days=1) )
