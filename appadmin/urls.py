from django.urls import path, include
from .views import AssignRollNoView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register(r'assign-rollno', AssignRollNoViewSet, basename='AssignRollNo')

urlpatterns = [
    # path('', include(router.urls)),
    path('update-rollno/<str:student_id>/', AssignRollNoView.as_view()),
]
