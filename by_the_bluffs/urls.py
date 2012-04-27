from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import home
from crags.views import climb_view, crag_view, area_view

admin.autodiscover()

urlpatterns = patterns('',
                       (r'^$', home),
                       (r'^climbs/(\d+)/$', climb_view),
                       (r'^crags/(\d+)/$', crag_view),
                       (r'^areas/(\d+)/$', area_view),
    # url(r'^by_the_bluffs/', include('by_the_bluffs.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       url(r'^admin/', include(admin.site.urls)),
)
