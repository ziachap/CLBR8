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
    url(r'^follow/(?P<username>\w+)/$', views.follow, name='follow'),
    url(r'^unfollow/(?P<username>\w+)/$', views.unfollow, name='unfollow'),
    url(r'^accept_offer/(?P<id>[0-9]+)/(?P<username>\w+)/$', views.accept_offer, name='accept_offer'),

    url(r'^profile/(?P<username>\w+)/$', views.profile, name='profile'),
    url(r'^profile/(?P<username>\w+)/listings/$', views.profile_projects, name='profile_projects'),

    url(r'^listing/([0-9]+)/$', views.listing, name='listing'),
    url(r'^edit_listing/([0-9]+)/$', views.edit_listing, name='edit_listing'),
    url(r'^delete_listing/([0-9]+)/$', views.delete_listing, name='delete_listing'),
    url(r'^new_listing/$', views.new_listing, name='new_listing'),
    url(r'^new_offer/([0-9]+)/$', views.new_offer, name='new_offer'),

    url(r'^browse/$', views.browse_map, name='browse_map'),
    url(r'^about/$', views.about, name='about'),

    #url(r'^inbox/$', views.inbox, name='inbox'), #OLD
    url(r'^inbox/([0-9]+)/$', views.inbox, name='inbox'),
    url(r'^inbox/$', views.inbox_default, name='inbox_default'),
    url(r'^conversation/([0-9]+)/$', views.conversation, name='conversation'),

    url(r'^settings_user/$', views.settings_user, name='settings_user'),
    url(r'^settings_profile/$', views.settings_profile, name='settings_profile'),

    url(r'^admin/', include(admin.site.urls)),
)