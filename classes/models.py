from django.db import models

# from course.models import Course
# from student.models import Student

class Classes(models.Model):
    name = models.CharField(max_length=20, null=False)
    class_id = models.PositiveIntegerField(null=False)
    description = models.TextField(null=False)
    capacity = models.PositiveSmallIntegerField(default=0000)
    occupied = models.BooleanField(default=False)
    equipments = models.TextField(null=False)
    course_code = models.PositiveSmallIntegerField(unique=True)
   

    def __str__(self):
           return f"{self.name} {self.capacity}"

 