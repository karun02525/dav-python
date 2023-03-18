from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.db import IntegrityError
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from .serializers import UserSerializer


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


class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status': 403, 'errors': serializer.errors, 'mess': 'something went wrong'})

        serializer.save()
        user = User.objects.get(username=serializer.data ['username'])
        token, created = Token.objects.get_or_create(user=user)
        return Response({'status': 200, 'payload': serializer.data, 'token': str(token)})


class LoginAV(APIView):
    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        user = authenticate(request, username=data['username'], password=data['password'])
        if user is None:
            return Response({'error': 'please check username or password!'})
        else:
            try:
                token = Token.objects.get(user=user)
            except:
                token = Token.objects.create(user=user)
            return Response({'token': str(token)}, status=status.HTTP_200_OK)
