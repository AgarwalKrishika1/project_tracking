from rest_framework import serializers
from apps.projects.models import Client, Projects


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
        fields = ['client_name', 'client_mobile', 'client_email', 'projects']


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'
