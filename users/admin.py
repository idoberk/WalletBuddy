from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Profile

# Register your models here.
class CustomUserAdmin(UserAdmin):
	model = CustomUser
	list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
	list_filter = ('is_staff', 'is_active')
	fieldsets = (
		(None, {'fields': ('username', 'email', 'password')}),
		('Personal Info', {'fields': ('first_name', 'last_name')}),
		('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
		('Important dates', {'fields': ('last_login', 'date_joined')}),
	)
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_active')}
		 ),
	)
	search_fields = ('username', 'email',)
	ordering = ('username', 'email',)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)