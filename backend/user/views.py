from rest_framework import generics, permissions

from .serializers import *


class LoginAPIView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = EmailLoginSerializer

    def post(self, request, *args, **kwargs):
        s = EmailLoginSerializer(data=request.data)


class OTPLoginVerifyAPIView(generics.GenericAPIView):
    permission_classes = []
    serializer_class = OTPSerializer

    def post(self, request, *args, **kwargs):
        pass


class RegisterAPIView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        pass


class OTPRegisterVerifyAPIView(generics.GenericAPIView):
    permission_classes = []
    serializer_class = OTPSerializer
    
    def post(self, request, *args, **kwargs):
        pass


class ProfileAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfileSerializer
