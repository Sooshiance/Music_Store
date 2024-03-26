from rest_framework import serializers

from .models import User, Profile


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['pk', 'phone', 'email', 'username', 'full_name']


class EmailLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)


class OTPSerializer(serializers.Serializer):
    username = serializers.CharField(required=False)
    otp      = serializers.CharField(required=True)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
