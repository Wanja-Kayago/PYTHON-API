from django.urls import path
from .views import StudentListView
from .views import TeacherListView
from .views import CourseListView
from .views import ClassPeriodListView
from .views import ClassesListView

urlpatterns = [
    path("students/" ,StudentListView.as_view(),name="student_list_view"),
    path("teachers/" ,TeacherListView.as_view(),name="teacher_list_view"),
    path("courses/" ,CourseListView.as_view(),name="course_list_view"),
    path("classrooms/" ,ClassesListView.as_view(),name="classroom_list_view"),
    path("classperiods/" ,ClassPeriodListView.as_view(),name="classperiod_list_view"),
]



