from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from core.views import homepage
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^inscricao/',include('subscription.urls',namespace='subscription')),
    url(r'^(\d+)/sucesso/$', 'success', name='success'),
	url(r'^$', homepage),
)
urlpatterns += staticfiles_urlpatterns()
