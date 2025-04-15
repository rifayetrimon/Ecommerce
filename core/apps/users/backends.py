from django.contrib.auth.backends  import ModelBackend
from django.contrib.auth import get_user_model


class PhoneBackend(ModelBackend): # custom authentication backend for phone number
    def authenticate(self, request, phone_number=None, password=None, **kwargs):
        User = get_user_model()
        if phone_number is None:
            phone_number = kwargs.get('username')
        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None
    