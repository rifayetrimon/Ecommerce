from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from django.utils import timezone


User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer): # user registration serializer
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('phone_number', 'password', 'password2')
    
    def validate_phone_number(self, value):
        if User.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("User with this phone number already exists")
        return value
    
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match")
        return data
    
    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user
    

class UserDetailsSearializer(serializers.ModelSerializer): # user details serializer
    class Meta:
        model = User
        fields = ('phone_number', 'username', 'email', 'first_name', 'last_name')


class PhoneTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'phone_number'

    def validate(self, attrs): 
        phone_number = attrs.get('phone_number')
        password = attrs.get('password')
        if phone_number and password:
           attrs[self.username_field] = phone_number
        else:
            raise serializers.ValidationError("Phone number and password are required")
        
        data = super().validate(attrs)
        
        exp_timestamp = self.get_token(self.user)['exp']
        current_timestamp = int(timezone.now().timestamp())
        data['expires_in'] = exp_timestamp - current_timestamp

        return data


class CustomRefreshTokenSearializer(TokenRefreshSerializer): # refresh token serializer 
    def validate(self, attrs):
        refresh_token = self.initial_data.get('refresh')
        refresh_obj = RefreshToken(refresh_token)

        new_access_token = refresh_obj.access_token
        data = {'access': str(new_access_token)}

        exp_timestamp = new_access_token['exp']
        current_timestamp = int(timezone.now().timestamp())
        data['expires_in'] = exp_timestamp - current_timestamp

        return data