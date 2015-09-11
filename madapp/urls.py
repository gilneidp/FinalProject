from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

# ... the rest of your URLconf goes here ...

urlpatterns = [
    url(r'^accounts/login/$', auth_views.login),
    url(r'^$', 'madapp.mad.views.index'),
    url(r'^home/$', 'madapp.mad.views.index'),
    #url(r'^config/$', include(admin.site.urls)),
    url(r'^about/$', 'madapp.mad.views.about'),
    url(r'^honeypotstatus/$', 'madapp.mad.views.honeypotstatus'),
    url(r'^poxstatus/$', 'madapp.mad.views.poxstatus'),
    url(r'^tempflows/$', 'madapp.mad.views.tempflows'),
    url(r'^poxlogs/$', 'madapp.mad.views.poxlogs'),
    url(r'^admin/', include(admin.site.urls)),
]
