from rest_framework import serializers
from apps.master.models import ProjectCategory


class ProjectCategorySerializer(serializers.ModelSerializer):
    category = serializers.ChoiceField(ProjectCategory.get_project_categories())

    class Meta:
        model = ProjectCategory
