from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views import View
# from django.contrib.auth.models import User
# from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer, RegisterUserSerializer, LoginSerializer


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class RegisterUserView(ModelViewSet):
    queryset = get_user_model().objects.all()
    http_method_names = ["post"]
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterUserSerializer


class LoginView(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    http_method_names = ["post"]
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer

    @api_view(['POST'])
    def verify_user(request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            try:
                user_profile = User.objects.get(
                    email=email,
                    password=password
                )
                user_profile.save()

                return Response({'message': 'User verified and upload_certificate uploaded successfully.'},
                                status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response({'message': 'User verification failed. Invalid code or details,try agan.'},
                                status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)









    #
    # def post(self, request):
    #     serializer = LoginSerializer(data=request.data)
    #
    #     if serializer.is_valid():
    #         user = serializer.validated_data['user']
    #         return Response({'message': 'Login successful', 'user_id': user.id}, status=status.HTTP_200_OK)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def get(self, request):
    #     #         serializer = LoginSerializer(data=request.data)
    #     #         if serializer.is_valid():
    #     #             email = serializer.validated_data['email']
    #     #             password = serializer.validated_data['password']
    #     #             user = authenticate(email=email, password=password)
    #     #
    #     #             if user is not None:
    #     #                 return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
    #     #             else:
    #     #                 return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    #     #
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # serializer = UserSerializer(data=request.data)
    # if serializer.is_valid():
    #     user = serializer.save()
    #     return Response({'user': user.email})
    # else:
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #     if user is not None:
    #         login(request, user)
    #         return HttpResponseRedirect('/login/')  # Replace with your desired URL
    #     else:
    #         return HttpResponse('Invalid login credentials')
    # return HttpResponse('Please use the login form')

# class LoginUserView(viewsets.ModelViewSet):
#     queryset = get_user_model().objects.all()
#     http_method_names = ["get", "post"]
#     permission_classes = [permissions.AllowAny]
#     serializer_class = LoginSerializer
#
#     def get(self, request):
#         serializer = LoginSerializer(data=request.data)
#         if serializer.is_valid():
#             email = serializer.validated_data['email']
#             password = serializer.validated_data['password']
#             user = authenticate(email=email, password=password)
#
#             if user is not None:
#                 return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
#             else:
#                 return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
