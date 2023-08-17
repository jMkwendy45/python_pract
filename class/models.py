from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=12)
    password = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)

#
# from django.contrib.auth.views import LoginView, RegisterView
# from django.contrib.auth.forms import UserCreationForm
# from django.shortcuts import render, redirect
#
#
# class MyLoginView(LoginView):
#     template_name = 'login.html'
#
#
# class MyRegisterView(RegisterView):
#     template_name = 'register.html'
#     form_class = UserCreationForm
#
#     def form_valid(self, form):
#         form.save()
#         return redirect('login')
