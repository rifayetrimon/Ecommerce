from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from core.apps.users.serializers import UserRegistrationSerializer, UserDetailsSearializer, PhoneTokenObtainPairSerializer, CustomRefreshTokenSearializer


User = get_user_model()

class UserRegistrationView(generics.CreateAPIView): # user registration view
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer


class UserDetailsView(generics.RetrieveAPIView): # user details view
    serializer_class = UserDetailsSearializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class PhoneTokenObtainPairView(TokenObtainPairView): # phone token obtain pair view
    serializer_class = PhoneTokenObtainPairSerializer


class CustomRefreshTokenView(TokenRefreshView): # custom refresh token view
    serializer_class = CustomRefreshTokenSearializer
