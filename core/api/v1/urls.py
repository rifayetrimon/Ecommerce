
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('users/', include('core.api.v1.users.urls'))
]
