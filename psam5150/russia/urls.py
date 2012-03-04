# -*- coding: UTF-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'russia.views.signuphome', name='signup_main'),
    url(r'^helloworld/$', 'russia.views.helloworld', name='hello_world'),
    url(r'^sign_up/$', 'russia.views.sitesignup', name='site_signup'),
    url(r'^hello$', 'russia.views.hello', name='hello'),
    url(r'^contactdetails/$', 'russia.views.sitecontactdetails', name='site_contactdetails'),
)

# as view instead of the name


