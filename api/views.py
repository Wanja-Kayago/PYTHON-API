from django.shortcuts import render
from rest_framework.views import APIView
from student.models import Student
from teacher.models import Teacher
from course.models import Course
from classes.models import Classes
from classperiod.models import ClassPeriod


# from .serializers import StudentSerializer
# from .serializers import TeacherSerializer
# from .serializers import ClassroomSerializer
# from .serializers import ClassPeriodSerializer
# from .serializers import CourseSerializer
# from rest_framework.response import Response

from .serializers import StudentSerialiazer
from .serializers import TeacherSerialiazer
from .serializers import CourseSerialiazer
from .serializers import ClassesSerialiazer
from .serializers import ClassPeriodSerialiazer

class StudentListView(APIView):
    def get(self, request):
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)
    


class TeacherListView(APIView):
    def get(self, request):
        teacher = Teacher.objects.all()
        serializer = TeacherSerializer(teacher, many=True)
        return Response(serializer.data)
    

class ClassesListView(APIView):
    # def get(self, request):
    #     classs = Classes.objects.all()
    #     serializer = ClassesSerializer(classs, many=True)
    #     return Response(serializer.data)
    

class ClassPeriodListView(APIView):
    def get(self, request):
        classperiod = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(classperiod, many=True)
        return Response(serializer.data)
    

class CourseListView(APIView):
    def get(self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)

# Create your views here.
