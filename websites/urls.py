from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'websites.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^property/(?P<property_id>\w+)/edit/$', 'hometracker.views.edit_property', name='edit_property'),
    url(r'^property/(?P<property_id>\w+)/delete/$', 'hometracker.views.delete_property', name='delete_property'),
    url(r'^propertynotes/(?P<property_id>\w+)/edit/$', 'hometracker.views.edit_propertynotes', name='edit_propertynotes'),
    url(r'^propertynotes/(?P<property_id>\w+)/delete/$', 'hometracker.views.delete_propertynotes', name='delete_propertynotes'),
    url(r'^propertynotes/new/$', 'hometracker.views.new_propertynotes', name='new_propertynotes'),
    url(r'^index/$', 'hometracker.views.index', name='index'),
    url(r'^register/$', 'hometracker.views.register', name='register'),
    url(r'^$', 'hometracker.views.profile', name='profile'),
    url(r'^faq/$', 'hometracker.views.faq', name='faq'),
    url(r'^map/$', 'hometracker.views.map', name='map'),
    url(r'^base/$', 'hometracker.views.base', name='base'),
    url(r'^properties/$', 'hometracker.views.properties', name='properties'),
    url(r'^property/new/$', 'hometracker.views.new_property', name='new_property'),
    url(r'^property/(?P<property_id>\w+)/$', 'hometracker.views.view_property', name='view_property'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    'django.contrib.auth.views.password_reset_confirm',
    name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)