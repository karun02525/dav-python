from django.urls import path, include
from .views import ClassesViewSet, StudentsViewSet, StudentFileUploadAV
from rest_framework.routers import DefaultRouter
from teacher.views import TeacherFileUploadAV

router = DefaultRouter()
router.register(r'classes', ClassesViewSet, basename='Classes')
router.register(r'students', StudentsViewSet, basename='Students')

urlpatterns = [
    path('admin/teacher-fileupload/', TeacherFileUploadAV.as_view()),
    path('admin/student-fileupload/', StudentFileUploadAV.as_view()),
    path('', include(router.urls)),
]
