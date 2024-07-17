
from django.db import models
import datetime
from teacher.models import Teacher

from student.models import Student

class Course(models.Model):
    name = models.CharField(max_length=35)
    description = models.CharField(max_length=100)
    fee = models.PositiveSmallIntegerField(default=0)
    course_code = models.PositiveSmallIntegerField(unique=True)
    content = models.TextField(null=False)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(default=datetime.date.today)
    duration_in_hours = models.DurationField(default=1)
    department = models.CharField(max_length=25)
    department_code = models.PositiveSmallIntegerField(unique=True)
    number_of_students = models.PositiveSmallIntegerField(default=0)
    student = models.ManyToManyField(Student, related_name='courses')
    teacher = models.ForeignKey(Teacher, on_delete = models.CASCADE, related_name='courses')

    def __str__(self):
           return f"{self.name} {self.course_code}"

