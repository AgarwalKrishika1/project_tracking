from django.contrib.auth.password_validation import validate_password
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

    class Meta:
        model = UserProfile
        # Cannot use both fields and exclude together
        # fields = '__all__'
        exclude = ['user']

#
# class UserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)
#     profile = UserProfileSerializer(required=True)
#     email = serializers.EmailField(write_only=True)
#
#     def validate_password(self, value):
#         validate_password(value)
#         return value
#
#     def create(self, validated_data):
#         user = UserProfile.objects.create(user=validated_data['user'],
#                                           email=validated_data['email'])
#         user.set_password(validated_data['password'])
#         user.save()
#         profile_data = validated_data.pop('profile', {})
#         profile_data['user'] = user
#         profile = UserProfile.objects.create(**profile_data)
#         profile.save()
#         return user
#
#     class Meta:
#         model = UserProfile
#         fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user