from django.urls import path,include
from .views import RegisterUser, LoginAV

urlpatterns = [
    path('register/', RegisterUser.as_view()),
    path('login/', LoginAV.as_view()),
]
