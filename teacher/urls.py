from django.urls import path, include
from .views import TeacherView, TeacherClassDetails
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register(r'teacher', TeacherViewSet, basename='Teacher')
# router.register(r'teacher-class-details', TeacherClassDetails, basename='TeacherClassDetails')


urlpatterns = [
    path('teachers', TeacherView.as_view()),
    path('teacher/<str:pk>', TeacherView.as_view()),
    # path('', include(router.urls))
]
