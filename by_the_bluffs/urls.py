from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'by_the_bluffs.views.home', name='home'),
    # url(r'^by_the_bluffs/', include('by_the_bluffs.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),


    url(r'^admin/', include(admin.site.urls)),
)
