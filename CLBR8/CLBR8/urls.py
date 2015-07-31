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
    url(r'^new_listing/$', views.new_listing, name='new_listing'),
    url(r'^browse/$', views.browse_map, name='browse_map'),
    url(r'^about/$', views.about, name='about'),

    url(r'^admin/', include(admin.site.urls)),
)