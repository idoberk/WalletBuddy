from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from .tokens import account_activation_token

def send_password_reset_email(request, associated_user):
	current_site = get_current_site(request)
	email_subject = 'Reset Your WalletBuddy Account Password'
	email_message = render_to_string('users/password_reset_email.html', {
		'user': associated_user,
		'domain': current_site,
		'uid': urlsafe_base64_encode(force_bytes(associated_user.pk)),
		'token': account_activation_token.make_token(associated_user),
		'protocol': 'https' if request.is_secure() else 'http'
	})

	email = EmailMessage(subject = email_subject,
	                     body = email_message,
	                     from_email = settings.EMAIL_HOST_USER,
	                     to = [associated_user.email]
	                     )

	email.content_subtype = "html"

	if email.send():
		messages.add_message(request,
		                     messages.SUCCESS,
		                     f"A password reset email has been sent to {associated_user.email}."
		                     )

	else:
		messages.add_message(request,
		                     messages.ERROR,
		                     f"An error occurred while sending the password reset email to {associated_user.email}."
		                     f"Please make sure you've entered a valid email address."
		                     )