from rest_framework import generics, permissions, response, status

from .models import User ,UserOTP
from .serializers import *
from .otp import otpToken


################### TODO : AUTH Section ###################


class LoginAPIView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer


class RegisterAPIView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        s = RegisterSerializer()
        if s.is_valid():
            email = s.validated_data["email"]
            username = s.validated_data["username"]
            phone = s.validated_data["phone"]
            full_name = s.validated_data["full_name"]
            password = s.validated_data["password"]
            user = User.objects.create(email=email,username=username,phone=phone,full_name=full_name,
                                       password=password)
            
            user.is_active = False
            user.set_password(password)
            user.save()
            otp = otpToken()
            UserOTP.objects.create(user=user,otp=otp).save()
            return response.Response(data=s.data, status=status.HTTP_201_CREATED)
        else:
            return response.Response(data=s.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


class OTPRegisterVerifyAPIView(generics.GenericAPIView):
    permission_classes = []
    serializer_class = OTPSerializer
    
    def post(self, request, *args, **kwargs):
        s = OTPSerializer(data=request.data)
        if s.is_valid():
            otp = s.validated_data["otp"]
            try:
                otp_user = UserOTP.objects.get(otp=otp)
                user = User.objects.get(email=otp_user)
                user.is_active = True
                user.save()
                return response.Response(data=s.data, status=status.HTTP_200_OK)
            except:
                return response.Response(data=s.errors, status=status.HTTP_404_NOT_FOUND)
        else:
            return response.Response(data=s.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfileSerializer


################### TODO : Password Reset Section ###################


class VerifyPhoneAPIView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = PhoneSerializer

    def post(self, request, *args, **kwargs):
        s = PhoneSerializer(data=request.data)


class VerifyOTPAPIView(generics.GenericAPIView):
    permission_classes = []
    serializer_class = OTPSerializer

    def post(self, request, *args, **kwargs):
        s = OTPSerializer(data=request.data)


class ChangePasswordAPIView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = [PasswordSerializer]

    def post(self, request, *args, **kwargs):
        s = PasswordSerializer(data=request.data)
