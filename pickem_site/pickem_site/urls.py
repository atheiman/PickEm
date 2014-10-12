from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	url(r'^pickem/', include('pickem_app.urls', namespace='pickem_app')),
	url(r'^accounts/', include('accounts_app.urls', namespace='accounts_app')),
	url(r'^admin/', include(admin.site.urls)),
)
