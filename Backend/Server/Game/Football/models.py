from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    age = models.PositiveIntegerField()
    country = models.CharField(max_length=200)
    student_id = models.IntegerField(unique=True)

    def __str__(self):
        return self.first_name

class Course(models.Model):
    course_code = models.CharField(max_length=50, unique=True)
    course_name = models.CharField(max_length=100)