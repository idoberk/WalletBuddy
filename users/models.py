from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from PIL import Image


# Create your models here.
class CustomUserManager(BaseUserManager):
	def create_user(self, email, username, password=None, **extra_fields):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')
		email = self.normalize_email(email)
		user = self.model(email=email, username = username, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password=None, **extra_fields):
		"""
		Creates and saves a new superuser with the given email and password.
		"""
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)
		extra_fields.setdefault('is_active', True)
		extra_fields.setdefault('email_verified', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError(_('Superuser should have is_staff as True'))

		if extra_fields.get('is_superuser') is not True:
			raise ValueError(_('Superuser should have is_superuser as True'))

		if extra_fields.get('is_active') is not True:
			raise ValueError(_('Superuser should have is_active as True'))

		return self.create_user(email, username, password, **extra_fields)

class CustomUser(AbstractUser, PermissionsMixin):
	username = models.CharField(_('username'), max_length=30, unique=True, blank=False, null=False)
	first_name = models.CharField(_('first name'), max_length=30, blank=False, null=False)
	last_name = models.CharField(_('last name'), max_length=30, blank=False, null=False)
	email = models.EmailField(_('email address'), unique=True, blank=False, null=False)
	email_verified = models.BooleanField(_('email verified'), default=False, help_text = _('Designates whether this user has verified their email address.'))
	is_active = models.BooleanField(_('active'), default=False)
	is_staff = models.BooleanField(_('staff status'), default=False)
	date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

	objects = CustomUserManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

	def __str__(self):
		return self.username


class Profile(models.Model):
	user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.user.username}'s profile"
	
	# def save(self, *args, **kwargs):
	# 	super().save(*args, **kwargs)
	# 	img = Image.open(self.image.path)
	#
	# 	if img.height > 300 or img.width > 300:
	# 		output_size = (300, 300)
	# 		img.thumbnail(output_size)
	# 		img.save(self.image.path)