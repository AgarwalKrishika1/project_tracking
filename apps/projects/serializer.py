from rest_framework import serializers
from apps.projects.models import Client, Projects, Developer
from apps.users.serializer import UserProfileSerializer


class ClientSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        client_mobile = str(data.get('client_mobile'))
        if len(client_mobile) < 10:
            raise ValueError("Mobile number invalid")
        print(data)
        return data

    projects = serializers.PrimaryKeyRelatedField(many=True, queryset=Projects.objects.all())

    class Meta:
        model = Client
        fields = ['id', 'name', 'mobile', 'email', 'projects']


class ProjectsSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    # for creating and saving fk and showing name instead of id of fk
    project_manager = serializers.PrimaryKeyRelatedField(queryset=Projects.objects.all(),
                                                         many=True), serializers.StringRelatedField()

    class Meta:
        model = Projects
        fields = ['id', 'name', 'description', 'category', 'status', 'logo', 'project_manager', 'created_at',
                  'updated_at']


class ProjectsReadOnlySerialzier(serializers.ModelSerializer):
    def create(self, validated_data):
        pass

    project_manager = UserProfileSerializer()

    class Meta:
        model = Projects
        fields = ['id', 'name', 'description', 'category', 'status', 'logo', 'project_manager', 'created_at',
                  'updated_at']


class ProjectDeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = ['id', 'project', 'user']
