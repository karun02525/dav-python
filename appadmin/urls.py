from django.urls import path, include
from .views import AssignRollNoViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'assign-rollno', AssignRollNoViewSet, basename='AssignRollNo')

urlpatterns = [
    path('', include(router.urls)),
]
