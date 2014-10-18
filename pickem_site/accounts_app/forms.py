from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
# PasswordChangeForm, PasswordResetForm, SetPasswordForm, UserChangeForm, UserCreationForm

from .models import User



class RegisterForm(forms.Form):
	username = forms.RegexField(
		label='Username',
		max_length=30,
		regex=r'^[a-z0-9-_]+$',
		error_messages={'required': 'Please enter your name', 'invalid': 'Lowercase alphanumeric characters and underscores and dashes only (a-z, 0-9, _, -)'},
	)
	password = forms.CharField(
		label='Password',
		max_length=30,
		widget=forms.PasswordInput,
	)
	confirm_password = forms.CharField(
		label='Confirm Password',
		max_length=30,
		widget=forms.PasswordInput,
	)
	
	def clean(self):
		password = self.cleaned_data.get('password')
		confirm_password = self.cleaned_data.get('confirm_password')

		if password != confirm_password:
			raise forms.ValidationError("Passwords don't match")

		return self.cleaned_data



class ProfileForm(forms.Form):
	username = forms.RegexField(
		label='Username',
		max_length=30,
		regex=r'^[a-zA-Z0-9-_]+$',
		error_messages={'required': 'Please enter your name', 'invalid': 'Alphanumeric, underscores, and dashes only (a-z, A-Z, 0-9, _, -)'},
	)
	first_name = forms.RegexField(
		label='First Name',
		max_length=30,
		regex=r'^[a-zA-Z-_]+$',
		error_messages={'invalid': 'Alphabetical, underscores, and dashes only (a-z, A-Z, _, -)'},
		required=False,
	)
	last_name = forms.RegexField(
		label='First Name',
		max_length=30,
		regex=r'^[a-zA-Z-_]+$',
		error_messages={'invalid': 'Alphabetical, underscores, and dashes only (a-z, A-Z, _, -)'},
		required=False,
	)
	email = forms.EmailField(
		label='First Name',
		max_length=50,
		required=False,
	)
	password = forms.CharField(
		label='Password',
		max_length=30,
		widget=forms.PasswordInput,
		required=False,
	)
	confirm_password = forms.CharField(
		label='Confirm Password',
		max_length=30,
		widget=forms.PasswordInput,
		required=False,
	)
	
	def clean(self):
		password = self.cleaned_data.get('password')
		confirm_password = self.cleaned_data.get('confirm_password')

		if password and password != confirm_password:
			raise forms.ValidationError("Passwords don't match")

		return self.cleaned_data

# class UserForm(ModelForm):
# 	class Meta:
# 		model = User
# 		fields = [
# 			'username',
# 			'email',
# 			'first_name',
# 			'last_name',
# 			'password',
# 		]



# class UserForm(forms.Form):
# 	# username = forms.CharField(label='Username', max_length=30, required=True)
# 	username = forms.RegexField(label=("Username"),
# 		max_length=30,
# 		regex=r'[a-zA-Z0-9_-]+',
# 		error_messages={
# 			'required': 'Username is required',
# 			'invalid': 'Letters, numbers, underscore, and dashes only. Less than 30 chars.'
# 		},
# 	)
# 	# first_name = forms.RegexField(label=("First name"),
# 	# 	max_length=30,
# 	# 	regex=r'[a-zA-Z]+',
# 	# 	required=True,
# 	# 	error_messages={'invalid': 'Letters only.'},
# 	# )
# 	# last_name = forms.RegexField(label=("Last name"),
# 	# 	max_length=30,
# 	# 	regex=r'[a-zA-Z]+',
# 	# 	required=True,
# 	# 	error_messages={'invalid': 'Letters only.'},
# 	# )
# 	email = forms.EmailField(
# 		label='Email',
# 		max_length=75,
# 		required=False,
# 	)
# 	password = forms.CharField(widget=forms.PasswordInput, max_length=30)
# 	confirm_password = forms.CharField(widget=forms.PasswordInput, max_length=30)
	
# 	def clean(self):
# 		cleaned_data = super(UserForm, self).clean()
# 		password = cleaned_data.get('password')
# 		confirm_password = cleaned_data.get('confirm_password')
		
# 		if password != confirm_password:
# 			raise forms.ValidationError("Passwords don't match")
		
# 		if User.objects.filter(username=cleaned_data.get('username')).count() != 0:
# 			raise forms.ValidationError("Username '%s' is already taken" % cleaned_data.get('username'))
		
# 		return self.cleaned_data



