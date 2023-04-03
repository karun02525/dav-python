from django.urls import path
from .views import (StudentAttendance)

urlpatterns = [
    path('create-students-attendance/', StudentAttendance.as_view()),
    path('student-attendance/<int:pk>/', StudentAttendance.as_view()),
]
