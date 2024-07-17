from django.db import models
import datetime
# Create your models here.

class ClassPeriod(models.Model):
    start_time = models.DateField(datetime.date.today)
    end_time = models.TimeField()
    course = models.CharField(max_length=30)
    classroom = models.CharField(max_length=30)
    day_of_the_week = models.DateField(datetime.date.today)
    


    def __str__(self):
           return f"{self.course} {self.classroom}"




