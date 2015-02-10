from django.conf.urls import patterns, include, url

urlpatterns = patterns('series.views',
    url(r'^$', 'home'),
    url(r'^(?P<serie_id>\d+)/$', 'serie'),
    url(r'^topic/(?P<topic_id>\d+)$', 'topic'),
    url(r'^submission/(?P<submission_id>\d+)$', 'submission'),
    url(r'^submission/(?P<submission_id>\d+)/vote$', 'submission_vote'),
    #url(r'^$', 'serie_view'),

)
