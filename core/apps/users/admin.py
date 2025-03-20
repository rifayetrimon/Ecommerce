from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.apps.users.models import User

# Register your models here.

class CustomUserAdmin(UserAdmin):
    search_fields = ('email', 'username', 'phone_number')
    list_filter = UserAdmin.list_filter
    list_display = ('phone_no', 'username', 'email', 'first_name', 'last_name')


admin.site.register(User, CustomUserAdmin)