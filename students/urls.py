from django.urls import path, include
from .views import ClassesViewSet, StudentsView, StudentFileUploadAV, StudentsFindByClass
from rest_framework.routers import DefaultRouter
from teacher.views import TeacherFileUploadAV

router = DefaultRouter()
router.register(r'classes', ClassesViewSet, basename='Classes')
router.register(r'', ClassesViewSet, basename='Classes')

urlpatterns = [
    path('classes-students/<str:class_id>/', StudentsFindByClass.as_view(), name='find students by class id '),
    path('students/', StudentsView.as_view()),
    path('student/<str:pk>/', StudentsView.as_view()),
    path('admin/teacher-fileupload/', TeacherFileUploadAV.as_view()),
    path('admin/student-fileupload/', StudentFileUploadAV.as_view()),
    path('', include(router.urls)),
]
