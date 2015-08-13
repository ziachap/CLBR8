from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from App import views

urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    }),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT,
    }),

    url(r'^$', views.index, name='index'),
    url(r'^feed/$', views.feed, name='feed'),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^profile/(?P<username>\w+)/$', views.profile, name='profile'),
    url(r'^listing/([0-9]+)/$', views.listing, name='listing'),
    url(r'^edit_listing/([0-9]+)/$', views.edit_listing, name='edit_listing'),
    url(r'^delete_listing/([0-9]+)/$', views.delete_listing, name='delete_listing'),
    url(r'^new_listing/$', views.new_listing, name='new_listing'),
    url(r'^new_offer/([0-9]+)/$', views.new_offer, name='new_offer'),
    url(r'^browse/$', views.browse_map, name='browse_map'),
    url(r'^about/$', views.about, name='about'),

    url(r'^settings_user/$', views.settings_user, name='settings_user'),
    url(r'^settings_profile/$', views.settings_profile, name='settings_profile'),

    url(r'^admin/', include(admin.site.urls)),
)