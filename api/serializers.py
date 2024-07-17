

from rest_framework import serializers
from student.models import Student
from teacher.models import Teacher
from course.models import Course
from classes.models import Classes
from classperiod.models import ClassPeriod

class StudentSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class TeacherSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"

class CourseSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

class ClassesSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = "__all__"

class ClassPeriodSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = ClassPeriod
        fields = "__all__"