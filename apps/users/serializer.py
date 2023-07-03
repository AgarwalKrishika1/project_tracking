from apps.users.models import  UserProfile, CustomUser
from rest_framework import serializers


class UserProfileSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        mobile = str(data.get('mobile'))
        if len(mobile) < 10:
            raise ValueError("Mobile number invalid")
        print(data)
        return data

    class Meta:
        model = UserProfile
        fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'