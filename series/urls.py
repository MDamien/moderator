from django.conf.urls import patterns, include, url

urlpatterns = patterns('series.views',
    url(r'^$', 'home'),
    url(r'^(?P<serie_id>\d+)/$', 'serie_view'),
    url(r'^\d+/(?P<topic_id>\d+)$', 'topic_view'),
    url(r'^\d+/\d+/(?P<submission_id>\d+)$', 'submission_view'),
    #url(r'^$', 'serie_view'),

)
