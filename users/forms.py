from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm, PasswordResetForm
from .models import CustomUser, Profile

class CustomUserRegistrationForm(UserCreationForm):
	email = forms.EmailField(required = True, widget = forms.EmailInput(attrs = {
		'class': 'form-control',
		'placeholder': 'Email'
	}))

	first_name = forms.CharField(widget = forms.TextInput(attrs = {
		'class': 'form-control',
		'placeholder': 'First Name'
	}))

	last_name = forms.CharField(widget = forms.TextInput(attrs = {
		'class': 'form-control',
		'placeholder': 'Last Name'
	}))

	username = forms.CharField(widget = forms.TextInput(attrs = {
		'class': 'form-control',
		'placeholder': 'Username'
	}))

	password1 = forms.Field(widget = forms.PasswordInput(attrs = {
		'class': 'form-control',
		'placeholder': 'Password'
	}), label = "Password")

	password2 = forms.Field(widget = forms.PasswordInput(attrs = {
		'class': 'form-control',
		'placeholder': 'Confirm Password'
	}), label = "Confirm Password")

	class Meta:
		model = CustomUser
		fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

	def clean(self):
		cleaned_data = super().clean()

		# Ensure that the email is unique
		email = cleaned_data.get('email')
		if email and CustomUser.objects.filter(email=email).exists():
			self.add_error('email', 'A user with this email already exists.')

		return cleaned_data


	def save(self, commit=True):
		instance = super().save(commit=False)
		instance.username = self.cleaned_data['username']
		if commit:
			instance.save()
		return instance

class UserUpdateForm(ModelForm):
	class Meta:
		model = CustomUser
		fields = ['email']

class ProfileUpdateForm(ModelForm):
	class Meta:
		model = Profile
		fields = ['image']

class SetPassForm(SetPasswordForm):
	class Meta:
		model = CustomUser
		fields = ['new_password1', 'new_password2']

class PassResetForm(PasswordResetForm):
	def __init__(self, *args, **kwargs):
		super(PasswordResetForm, self).__init__(*args, **kwargs)