from django.conf.urls import patterns, include, url
from django.contrib import admin
from App import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/(?P<username>\w+)/$', views.profile, name='profile'),
    url(r'^browse/$', views.browse_map, name='browse_map'),
    #url(r'^profile/(?P<username>\w+)', views.profile, name='profile'),

    url(r'^admin/', include(admin.site.urls)),

)
