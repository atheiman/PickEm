from django.conf.urls import patterns, url

from accounts_app import views

urlpatterns = patterns('',
	# Login
	url(
		r'^login\/?$',
		views.custom_login,
		{'template_name': 'accounts_app/login.html'},
		name='login',
	),
	
	# Logout
	url(
		r'^logout\/?$',
		views.logout_view,
		{'next_page': '/accounts/login'},
		name='logout',
	),
	
	# Register
	url(
		r'^register\/?$',
		views.register,
		name='register',
	),
	
	# Profile
	url(
		r'^profile\/?$',
		views.profile,
		name='profile',
	),
)
