from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Profile


class Admin(UserAdmin):
    list_display = ['phone', 'email', 'is_active']
    filter_horizontal = []
    list_filter = []
    fieldsets = []


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'email']


admin.site.register(User, Admin)

admin.site.register(Profile, ProfileAdmin)
