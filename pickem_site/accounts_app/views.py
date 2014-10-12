from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import login as login_view, logout as logout_view
# from django.contrib.auth.views import password_change
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *



def custom_login(request, **kwargs):
	if request.user.is_authenticated():
		return HttpResponseRedirect(reverse('accounts_app:profile'))
	else:
		return login_view(request, **kwargs)



def register(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect(reverse('accounts_app:profile'))
	if request.method == 'POST':
		
		# create a form instance and populate it with data from the request
		form = RegisterForm(request.POST)
		
		if form.is_valid():
			
			# create a new user
			new_user = User.objects.create_user(username=form.cleaned_data['username'])
			new_user.set_password(form.cleaned_data['password'])
			new_user.save()
			
			# login after creation
			new_user = authenticate(
				username = form.cleaned_data['username'],
				password = form.cleaned_data['password'],
			)
			login(request, new_user)
			
			# redirect
			return HttpResponseRedirect(reverse('accounts_app:profile'))
	
	else:
		form = RegisterForm()
	
	return render(request, 'accounts_app/register.html', {'form': form})



@login_required
def profile(request):
	
	user = request.user
	message = ""
	
	current_info = {
		'username': user.username,
		'first_name': user.first_name,
		'last_name': user.last_name,
		'email': user.email,
	}
	
	# return HttpResponse("this is the user profile page for username '%s'. update first, last, email, username, and password here." % request.user.username)
	if request.method == 'POST':
		
		# create a form instance and populate it with data from the request
		form = ProfileForm(request.POST)
		
		if form.is_valid():
			
			if form.cleaned_data['username'] != user.username:
				user.username = form.cleaned_data['username']
			
			if form.cleaned_data['first_name'] != user.first_name:
				user.first_name = form.cleaned_data['first_name']
			
			if form.cleaned_data['last_name'] != user.last_name:
				user.last_name = form.cleaned_data['last_name']
			
			if form.cleaned_data['email'] != user.email:
				user.email = form.cleaned_data['email']
			
			if form.cleaned_data['password'] != user.password and form.cleaned_data['password'] != "":
				user.set_password(form.cleaned_data['password'])
			
			user.save()
			message += "Profile updated."
			
			return render(request, 'accounts_app/profile.html', {'form': form, 'message': message})
			
	else:
		form = ProfileForm(current_info)
	
	return render(request, 'accounts_app/profile.html', {'form': form})