from django.conf.urls import patterns, include, url
from tfeed.views import hello, trick, docs

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^tricks/$', trick),
	url(r'^docs/$', docs),
	url(r'^$', hello),
    # Examples:
    # url(r'^$', 'tfeed.views.home', name='home'),
    # url(r'^tfeed/', include('tfeed.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
