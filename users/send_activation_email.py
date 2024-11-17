from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from .tokens import account_activation_token

def send_activation_email(request, user):
	current_site = get_current_site(request)
	email_subject = 'Activate Your WalletBuddy Account'
	email_message = render_to_string('users/activation_email.html', {
		'user': user,
		'domain': current_site,
		'uid': urlsafe_base64_encode(force_bytes(user.pk)),
		'token': account_activation_token.make_token(user),
		'protocol': 'https' if request.is_secure() else 'http'
	})

	email = EmailMessage(subject = email_subject,
	                     body = email_message,
	                     from_email = settings.EMAIL_HOST_USER,
	                     to = [user.email]
	                     )

	email.content_subtype = "html"

	if email.send():
		messages.add_message(request,
		                     messages.SUCCESS,
		                     f"An activation email has been sent to {user.email}."
		                     )

	else:
		messages.add_message(request,
		                     messages.ERROR,
		                     f"An error occurred while sending the activation email to {user.email}."
		                     f"Please make sure you've entered a valid email address."
		                     )