# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.views.static import serve as st
from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import include
from django.conf.urls.defaults import url
from django.contrib import admin
from django.conf import settings
#from w3af_webui.settings import MEDIA_ROOT

admin.autodiscover()

urlpatterns = patterns('w3af_webui.views',
    ('^check_url/$', 'check_url'),
    ('^post_ticket/$', 'post_ticket'),
    ('^mark_vuln_false_positive/$', 'mark_vuln_false_positive'),
    ('^show_report/(\d+)/$', 'show_report'),
    ('^http_transaction/(\d+)/$', 'show_http_transaction'),
    ('^show_report_txt/(\d+)/$', 'show_report_txt'),
    ('^stop_scan/$', 'stop_scan'),
    ('^user_settings/$', 'user_settings'),
    ('^run_now/$', 'run_now'),
    ('^w3af_webui/stats/$', 'stats'),
    ('^w3af_webui/target_stats/(\d+)/$', 'target_stats'),
    ('^$', 'root'),
    #('^admin/$', 'root'),
    (r'^static/(?P<path>.*)$', st, {'document_root': settings.STATIC_ROOT}),
    #(r'^media/(?P<path>.*)$', st, {'document_root': MEDIA_ROOT}),
    url(r'', include(admin.site.urls), name=''),
)
if settings.DEBUG:
    urlpatterns += patterns('',
            (r'^static/(?P<path>.*)$', 'django.views.static.serve', {
             'document_root': settings.STATIC_ROOT
             }),
            (r'^media/(?P<path>.*)$',
             'django.views.static.serve', {
             'document_root':
             settings.MEDIA_ROOT
             }),
            )
