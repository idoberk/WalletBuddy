from django.urls import path
from django.contrib.auth import views as auth_views
from users import views as user_views


app_name = 'users'

urlpatterns = [
	path('register/', user_views.register, name='register'),
	path('profile/', user_views.profile, name='profile'),
	path('login/', user_views.login_view, name='login'),
	path('logout/', user_views.logout_view, name='logout'),
	path('delete/', user_views.delete_user, name='delete'),
	path('password-reset/', user_views.password_reset_request, name= 'password_reset'),
	path('password-reset/done/',
	     auth_views.PasswordResetDoneView.as_view(
		     template_name = "users/password_reset_done.html"
	     ), name='password_reset_done'),
	path('password-reset-confirm/<uidb64>/<token>/', user_views.password_reset_confirm, name='password_reset_confirm'),
	path('password-reset-complete/',
	     auth_views.PasswordResetCompleteView.as_view(
		     template_name = "users/password_reset_complete.html"
	     ), name='password_reset_complete'),
	path('password-change/', user_views.password_change, name= 'password_change'),
	path('activate/<uidb64>/<token>/', user_views.activate_user, name='activate'),
]

