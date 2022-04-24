from unicodedata import name
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    date_of_birth = models.DateField()

    # Presenting each student by his name.

    def __str__(self):
        return self.name


class Course(models.Model):
    LEVEL = (
        ('B', 'Beginner'),
        ('I', 'Intermediate'),
        ('A', 'Advanced'),
        ('E', 'Expert'),
    )

    code = models.CharField(max_length=30)
    description = models.TextField()
    level = models.CharField(max_length=1, choices=LEVEL, blank=False, null=False, default='B')

    def __str__(self):
        return self.code


class Registration(models.Model):
    SHIFT = (
        ('M', 'Morning'),
        ('E', 'Evening'),
        ('N', 'Night'),
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    shift = models.CharField(max_length=1, choices=SHIFT, blank=False, null=False, default='M')
    