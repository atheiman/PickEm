from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout, password_change

from pickem_app import views

urlpatterns = patterns('',
	# /
	url(
		r'^$',
		views.index,
		name='index',
	),
	
	# /u/
	url(
		r'^u\/?$',
		views.users_list,
		name='users_list',
	),
	
	# /u/johndoe/
	url(
		r'^u/(?P<username>[a-z0-9_-]+)\/?$',
		views.user,
		name='user',
	),
	
	# /u/johndoe/w/4/
	url(
		r'^u/(?P<username>[a-z0-9_-]+)/w/(?P<week>[0-9]{1,2})\/?$',
		views.pickset,
		name='pickset',
	),
	
	# POST picks (modify picks in pickset)
	url(
		r'^api/pickset/(?P<pickset_id>\d+)\/?$',
		views.api_pickset,
		name='api_pickset',
	),
)
