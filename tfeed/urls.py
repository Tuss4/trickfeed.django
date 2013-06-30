from django.conf.urls import *


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'tfeed.views.trick'),
	url(r'^search/$', 'books.views.search'),
	url(r'^contact/$', 'contact.views.contact'),
	url(r'^success/$', 'favo.views.success'),
    url(r'^myfavs/$', 'favo.views.list_fav'),
    # Examples:
    # url(r'^$', 'tfeed.views.home', name='home'),
    # url(r'^tfeed/', include('tfeed.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
