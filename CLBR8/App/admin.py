from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from App.models import *

# Register your models here.
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (ProfileInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)