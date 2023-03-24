from django.contrib.auth import login, authenticate
from rest_framework.permissions import IsAuthenticated

from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.db import IntegrityError
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from .serializers import (UserRegisterSerializer, UserLoginSerializer, UserProfileSerializer,
                          UserChangePasswordSerializer, SendPasswordResetEmailSerializer, UserPasswordResetSerializer)
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, renderer_classes
from django.contrib.auth import authenticate
from .renderers import UserRenderer


#
# @csrf_exempt
# def signup(request):
#     try:
#         data = JSONParser().parse(request)
#         print(data['username'], data['password'])
#         user = User.objects.create_user(data['username'], data['password'])
#         user.save()
#         token = Token.objects.create(user=user)
#         return Response({'token': str(token)}, status=status.HTTP_201_CREATED)
#     except IntegrityError:
#         return Response({'error': 'username or password already taken'})

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {'refresh': str(refresh), 'access': str(refresh.access_token)}


class UserRegisterView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response({'status': 403, 'errors': serializer.errors, 'mess': 'something went wrong'})

        serializer.save()
        user = User.objects.get(email=serializer.data['email'])
        token = get_tokens_for_user(user)
        return Response({'status': 200, 'payload': serializer.data, 'token': token})


class UserLoginView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if not serializer.is_valid(raise_exception=True):
            print(serializer.errors)
            return Response({'status': 404, 'errors': serializer.errors, 'mess': 'something went wrong'})

        email = serializer.data.get('email')
        password = serializer.data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            token = get_tokens_for_user(user)
            payload = {'name': user.first_name + " " + user.last_name, 'email': user.email, 'mobile': user.mobile,
                       'user_type': user.user_type, 'user_verified': user.user_verified},
            return Response({'status': 200,
                             'message': 'login successfully',
                             'payload': payload,
                             'token': token},
                            status=status.HTTP_200_OK)
        else:
            return Response({'errors': {'non_field_errors': ['Email or password is not valid']}},
                            status=status.HTTP_404_NOT_FOUND)


class UserLogoutView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        status = request.user.auth_token.delete()
        return Response({'status': 404, 'mess': 'logout successfully delete'})


class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)


class UserChangePasswordView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        serializer = UserChangePasswordSerializer(data=data, context={'user': request.user})
        if serializer.is_valid(raise_exception=True):
            return Response({'message': 'Password changes successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SendPasswordResetEmailView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request):
        data = request.data
        serializer = SendPasswordResetEmailSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            return Response({'message': 'Password Reset link send. Please check your email '})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserPasswordResetView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, uid, token):
        data = request.data
        serializer = UserPasswordResetSerializer(data=data, context={'uid': uid, 'token': token})
        if serializer.is_valid(raise_exception=True):
            return Response({'message': 'Password Reset successfully '})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
