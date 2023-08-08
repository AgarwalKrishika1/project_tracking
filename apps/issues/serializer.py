from rest_framework import serializers
from apps.issues.models import Issues
from apps.users.models import UserProfile
from apps.users.serializer import UserProfileSerializer
from apps.projects.serializer import ProjectsSerializer, ProjectsReadOnlySerialzier


class IssueSerializer(serializers.ModelSerializer):
    # projects = serializers.PrimaryKeyRelatedField(queryset=Projects.objects.all(),
    #                                               many=True), serializers.StringRelatedField()
    user = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all(),
                                              many=True), serializers.StringRelatedField()

    class Meta:
        model = Issues
        fields = ['id', 'title', 'description', 'type', 'status', 'priority', 'projects', 'users']


class IssueReadOnlySerializer(serializers.ModelSerializer):
    projects = ProjectsReadOnlySerialzier()
    users = UserProfileSerializer(many=True)

    class Meta:
        model = Issues
        fields = ['id', 'title', 'description', 'type', 'status', 'priority', 'projects', 'users']
