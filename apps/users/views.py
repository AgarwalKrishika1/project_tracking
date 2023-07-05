from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from apps.users.serializer import UserProfileSerializer, UserSerializer
from apps.users.models import UserProfile, User


# Create your views here.
class UserProfileModelView(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    # def get_serializer_context(self):
    #     context = super(UserProfileModelView, self).get_serializer_context()
    #     context.update({"user": self.request.user})
    #     return context


# class UserModelViewSet(ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


    # def get_serializer_context(self):
    #     context = super().get_serializer_context()
    #     context['request'] = self.request
    #     return context

class UserCreate(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
