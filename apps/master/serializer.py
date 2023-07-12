from rest_framework import serializers
from apps.master.models import ProjectCategory
from apps.projects.models import Projects


class ProjectCategorySerializer(serializers.ModelSerializer):
    category = serializers.ChoiceField(ProjectCategory.get_project_categories())

    class Meta:
        model =  ProjectCategory