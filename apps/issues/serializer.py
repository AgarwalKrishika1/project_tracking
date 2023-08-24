from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.issues.models import Issue
from apps.users.models import UserProfile
from apps.users.serializer import UserProfileSerializer
from apps.projects.serializer import ProjectSerializer, ProjectReadOnlySerializer, ProjectUserSerializer
from apps.projects.models import ProjectUser


class IssueSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all(),
                                              many=True), serializers.StringRelatedField()

    class Meta:
        model = Issue
        fields = ['id', 'title', 'description', 'type', 'status', 'priority', 'projects', 'users']


class IssueReadOnlySerializer(serializers.ModelSerializer):
    projects = ProjectReadOnlySerializer()
    users = UserProfileSerializer(many=True)

    class Meta:
        model = Issue
        fields = ['id', 'title', 'description', 'type', 'status', 'priority', 'projects', 'users']
