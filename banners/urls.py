# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('banners.views',
    url(r'^$', 'banner_manager'),
)
