from apps.users.models import UserProfile
from django.contrib.auth.models import User
from rest_framework import serializers


class UserProfileSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        mobile = str(data.get('mobile'))
        if len(mobile) < 10:
            raise ValueError("Mobile number invalid")
        print(data)
        return data

    def create(self, validated_data):
        username = self.context.get('username')
        user = User.objects.create_user(username=username, email=None, password=None)
        user.save()
        user_profile = UserProfile(user_id=user.id, **validated_data)
        user_profile.save()
        return user_profile

    class Meta:
        model = UserProfile
        # Cannot use both fields and exclude together
        # fields = '__all__'
        exclude = ['user']


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'profile']

    def create(self, validated_data):
        profile_data = validated_data.pop('profile', {})
        password = validated_data.pop('password')

        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        # profile = UserProfile.objects.create(user=user, **profile_data)

        return user
