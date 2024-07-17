
from django.db import models
import datetime

from classes.models import Classes


class Student(models.Model):
    first_name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=20, null=False)
    email = models.EmailField(null=False)
    phone_number = models.CharField(max_length=15, unique=True)
    date_of_birth = models.DateField(default = '0000-00-00')
    code = models.PositiveSmallIntegerField(unique=True)
    country = models.CharField(max_length=20, null=True)
    profile = models.ImageField(null=False)
    student_gender = models.CharField(max_length=20)
    bio = models.TextField(default="I am a student")
    national_id = models.IntegerField(default=0)
    joining_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(default=datetime.date.today)
    parent = models.CharField(max_length=50)
    next_of_kin = models.CharField(max_length=50)
    parent_number = models.CharField(max_length=15)
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
           return f"{self.first_name} {self.last_name}"


