from django.shortcuts import render
from apps.projects.models import Projects
from apps.master.models import ProjectCategory
from apps.master.serializer import ProjectCategorySerializer
from rest_framework.viewsets import ModelViewSet


# Create your views here.


class ProjectCategoryViewSet(ModelViewSet):
    queryset = ProjectCategory.objects.all()
    serializer_class = ProjectCategorySerializer
