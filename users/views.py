from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, logout, get_user_model, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.utils.safestring import mark_safe
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from .forms import CustomUserRegistrationForm, UserUpdateForm, ProfileUpdateForm, SetPassForm, PassResetForm
from .models import CustomUser
from .tokens import account_activation_token
from .send_activation_email import send_activation_email
from .send_password_reset_email import send_password_reset_email


# Create your views here.
@csrf_protect
def register(request):
	form = CustomUserRegistrationForm()
	if request.method == "POST":
		form = CustomUserRegistrationForm(request.POST or None)
		if form.is_valid():
			user = form.save(commit = False)
			user.save()
			send_activation_email(request, user)
			return redirect('users:login')

	context = {'form': form}
	return render(request, 'users/register.html', context)


@csrf_protect
def login_view(request):
	if request.user.is_authenticated:
		messages.info(request, mark_safe(f"You are already logged in as <b>{request.user.username}</b>."))
		return redirect('app-home')

	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username = username, password = password)
		if user is not None:
			if user.email_verified:
				login(request, user = user)
				messages.add_message(request, messages.SUCCESS, f"Logged in as {user.username}.")
				return redirect('app-home')
			else:
				messages.add_message(request, messages.ERROR, f"Email is not verified, please verify your email address.")

		else:
			messages.add_message(request, messages.ERROR, f"Invalid username or password.")
	return render(request, 'users/login.html')


@login_required
def profile(request):
	if request.method == 'POST':
		user_form = UserUpdateForm(request.POST, instance = request.user)
		profile_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)

		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request, f"Your profile has been updated!")
			return redirect('users:profile')

	else:
		user_form = UserUpdateForm(instance = request.user)
		profile_form = ProfileUpdateForm(instance = request.user)
	context = {
		'user_form': user_form,
		'profile_form': profile_form
	}
	return render(request, 'users/profile.html', context)


@login_required
def logout_view(request):
	logout(request)
	messages.success(request, f"Logged out successfully!")
	return redirect('users:login')


@login_required
@csrf_protect
def delete_user(request):
	if request.method == 'POST':
		user = CustomUser.objects.get(username = request.user.username)
		user.delete()
		messages.add_message(request, messages.SUCCESS, f"Your account has been deleted.")
		return redirect('app-home')
	return render(request, 'users/delete_user.html')

@login_required
@csrf_protect
def password_change(request):
	user = request.user
	if request.method == 'POST':
		form = PasswordChangeForm(user, request.POST)
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.SUCCESS, f"Password has been successfully changed.")
			return redirect('users:login')
		else:
			for error in list(form.errors.values()):
				messages.add_message(request, messages.ERROR, error)

	form = PasswordChangeForm(user)
	context = {'form': form}
	return render(request, 'users/password_reset_confirm.html', context)

@csrf_protect
def password_reset_request(request):
	if request.method == "POST":
		form = PassResetForm(request.POST)
		if form.is_valid():
			user_email = form.cleaned_data['email']
			associated_user = CustomUser.objects.filter(email = user_email).first()
			if associated_user:
				send_password_reset_email(request, associated_user)
				return redirect('users:login')

	form = PassResetForm()
	context = {'form': form}
	return render(request, 'users/password_reset.html', context)

@csrf_protect
def password_reset_confirm(request, uidb64, token):
	try:
		uid = force_str(urlsafe_base64_decode(uidb64))
		user = CustomUser.objects.get(pk = uid)
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None

	if user and account_activation_token.check_token(user, token):
		if request.method == 'POST':
			form = SetPassForm(user, request.POST)
			if form.is_valid():
				form.save()
				messages.add_message(request, messages.SUCCESS, mark_safe(f"Password has been successfully set."))
				return redirect('users:login')
			else:
				for error in list(form.errors.values()):
					messages.add_message(request, messages.ERROR, error)

		form = SetPassForm(user)
		context = {'form': form}
		return render(request, 'users/password_reset_confirm.html', context)
	else:
		messages.add_message(request, messages.ERROR, f"Link is expired.")

	messages.add_message(request, messages.ERROR, f"Password reset failed. Redirecting back to home page.")
	return redirect('app-home')


def activate_user(request, uidb64, token):
	User = get_user_model()
	try:
		uid = force_str(urlsafe_base64_decode(uidb64))
		user = CustomUser.objects.get(pk = uid)

	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None

	if user and account_activation_token.check_token(user, token):
		user.is_active = True
		user.email_verified = True
		user.save()
		messages.add_message(request, messages.SUCCESS, f"Email verification successful! You can now log in.")
		return redirect('users:login')

	else:
		messages.add_message(request, messages.ERROR, f"Email verification failed.")

	return redirect('app-home')