from rest_framework import serializers
from apps.issues.models import Issue
from apps.users.models import UserProfile
from apps.users.serializer import UserProfileSerializer
from apps.projects.serializer import ProjectSerializer, ProjectReadOnlySerializer


class IssueSerializer(serializers.ModelSerializer):
    # projects = serializers.PrimaryKeyRelatedField(queryset=Projects.objects.all(),
    #                                               many=True), serializers.StringRelatedField()
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
