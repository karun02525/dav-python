from django.urls import path, include
from .views import TeacherViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'teacher', TeacherViewSet, basename='Teacher')

urlpatterns = [
    path('', include(router.urls))
]
