from rest_framework.test import APIClient, APITestCase
from rest_framework import response
from apps.users.models import UserProfile, User
from apps.projects.models import Projects

# def create_project(name):
#     project = Projects.objects.create_project(name=name)
#     return project


def create_userprofile(username, email, password,role):
    user = User.objects.create_user(username=username, email=email, password=password)
    user_profile = UserProfile.objects.create(user_id=user.id, role=role )
    return user_profile

