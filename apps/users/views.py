from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from apps.users.serializer import UserProfileSerializer, CustomUserSerializer
from apps.users.models import UserProfile, CustomUser


# Create your views here.
class UserProfileModelView(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer