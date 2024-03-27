from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User, Profile


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['pk', 'phone', 'email', 'username', 'password', 'full_name']


class OTPSerializer(serializers.Serializer):
    otp      = serializers.CharField(required=True)
    username = serializers.CharField(required=False)


class PhoneSerializer(serializers.Serializer):
    phone = serializers.CharField(required=True)


class PasswordSerializer(serializers.Serializer):
    passowrd         = serializers.CharField(required=True, write_only=True)
    passowrd_confirm = serializers.CharField(required=True, write_only=True)


class LoginSerializer(TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token["id"] = user.id
        token["email"] = user.email
        token["username"] = user.username 

        return token 


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
