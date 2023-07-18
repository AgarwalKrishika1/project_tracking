from rest_framework import serializers
from apps.projects.models import Client, Projects, Developer
from apps.users.models import UserProfile, User


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
        fields = ['name', 'mobile', 'email', 'projects']


class ProjectsSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    project_manager = serializers.StringRelatedField()
    class Meta:
        model = Projects
        fields = '__all__'

    def create(self, validated_data):
        data = super().create(validated_data)
        return data

    # def to_representation(self, instance):
    #     rep = super(ProjectsSerializer, self).to_representation(instance)
    #     rep['category'] = instance.category.name
    #     return rep


class ProjectDeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = '__all__'
