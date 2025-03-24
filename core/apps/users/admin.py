from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.apps.users.models import User

# Register your models here.

class CustomUserAdmin(UserAdmin):
    search_fields = ('email', 'username', 'phone_number')
    list_filter = UserAdmin.list_filter
    list_display = ('phone_no', 'username', 'email', 'first_name', 'last_name')

    fieldsets =(
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('email', 'phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(User, CustomUserAdmin)


