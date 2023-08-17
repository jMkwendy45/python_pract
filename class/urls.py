from django.contrib.auth.views import LoginView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterUserView, LoginView

router = DefaultRouter()
#
router.register(r'register', RegisterUserView, basename='register'),
router.register(r'login ', LoginView, basename='login')

urlpatterns = [
    path('', include(router.urls)),
    # path('login/', LoginView.as_view(), name='custom_login'),

]
