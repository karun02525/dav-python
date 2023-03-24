from django.urls import path, include
from .views import home
from teacher.views import TeacherFileUploadAV

urlpatterns = [
    path('', home),
]
