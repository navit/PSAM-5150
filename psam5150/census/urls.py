# -*- coding: UTF-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'census.views.censusinfophome', name='censustemp_main'),
    #url(r'^helloworld/$', 'russia.views.helloworld', name='hello_world'),
    #url(r'^sign_up/$', 'russia.views.sitesignup', name='site_signup'),
    #url(r'^hello$', 'russia.views.hello', name='hello'),
    #url(r'^$', 'russia.views.sitecontactdetails', name='site_contactdetails'),
    url(r'^ CensusInfo/$', 'census.views.sitecensusinfo', name='sitecensusinfo'),
    
   

)

