from django.contrib import admin
from django.conf import settings

from .models import Profile,User
# User = settings.AUTH_USER_MODEL


admin.site.register(Profile)
admin.site.register(User)
