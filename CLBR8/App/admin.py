from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from App.models import *

# Register your models here.
class ReviewInline(admin.TabularInline):
    model = Review
    can_delete = True
    extra = 0
    verbose_name_plural = 'review'

class ListingInline(admin.TabularInline):
    model = Listing
    can_delete = True
    extra = 0
    verbose_name_plural = 'listing'

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'

# Define a new User admin
class UserAdmin(UserAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name')
    inlines = (ProfileInline, ListingInline, ReviewInline, )

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner', 'genre', 'audio_file')
    fields = ('owner', 'title', 'price', 'description', 'genre', 'audio_file', 'longitude', 'latitude', 'address')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('summary', 'description')
    fields = ('author', 'recipient', 'summary', 'description', 'rating_1', 'rating_2', 'rating_3')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Review, ReviewAdmin)