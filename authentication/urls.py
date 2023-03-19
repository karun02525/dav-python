from django.urls import path, include
from .views import (UserRegisterView,UserLoginView, UserProfileView,
                    UserChangePasswordView,SendPasswordResetEmailView,UserPasswordResetView)

urlpatterns = [
    path('register/', UserRegisterView.as_view()),
    path('login/', UserLoginView.as_view()),
    path('profile/', UserProfileView.as_view()),
    path('change-password/', UserChangePasswordView.as_view(), name='change password'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),
]
