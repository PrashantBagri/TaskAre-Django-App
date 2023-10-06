from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import newUser
# Register your models here.

admin.site.register(newUser)