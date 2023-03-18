from django.urls import path, include
from .views import ClassesViewSet, StudentsViewSet, UserDocAdminViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'classes', ClassesViewSet, basename='Classes')
router.register(r'students', StudentsViewSet, basename='Students')
router.register(r'admin', UserDocAdminViewSet, basename='user-docs-detail')

urlpatterns = [
    path('', include(router.urls)),
]
