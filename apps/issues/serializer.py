from rest_framework import serializers
from apps.issues.models import Issues
from apps.users.models import UserProfile
from apps.projects.models import Projects


class IssueSerializer(serializers.ModelSerializer):
    projects = serializers.PrimaryKeyRelatedField(queryset=Projects.objects.all(),
                                                  many=True), serializers.StringRelatedField()
    user = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all(),
                                              many=True), serializers.StringRelatedField()

    class Meta:
        model = Issues
        fields = ['title', 'description', 'type', 'status', 'priority', 'projects', 'users']
