from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'russia.views.home', name='home'),
    url(r'^signup/', include('russia.urls')),

    url(r'^$', 'census.views.home', name='home'),
    url(r'^censustemp/', include('census.urls')),
    
    #url(r'^gameshow/', include('gameshow.urls')),
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)