from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from App.models import *

# Register your models here.
class ReviewInline(admin.TabularInline):
    model = Review
    can_delete = True
    extra = 0
    verbose_name_plural = 'review'

class OfferInline(admin.TabularInline):
    model = Offer
    can_delete = True
    extra = 0
    verbose_name_plural = 'offer'

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
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name')
    inlines = (ProfileInline, ListingInline, ReviewInline, OfferInline, )

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner', 'genre', 'audio_file')
    fields = ('owner', 'title', 'price', 'description', 'genre', 'listing_pic', 'audio_file', 'longitude', 'latitude', 'address')
    inlines = (OfferInline, )

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('summary', 'description')
    fields = ('author', 'recipient', 'summary', 'description', 'rating_1', 'rating_2', 'rating_3')

class OfferAdmin(admin.ModelAdmin):
    list_display = ('id', 'listing', 'user', 'description')
    fields = ('id', 'listing', 'user', 'description')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Offer, OfferAdmin)