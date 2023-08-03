from apps.comments import Comment
from rest_framework import serializers
from apps.users.models import UserProfile
from apps.issues.models import Issues


class CommentSerializer(serializers.ModelSerializer):
    created_by = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all())
    created_for = serializers.PrimaryKeyRelatedField(queryset=Issues.objects.all())

    class Meta:
        model = Comment
        fields = ['id', 'text', 'created_by', 'created_for', 'created_at', 'updated_at']
