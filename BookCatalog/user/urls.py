from django.urls import path
from django.contrib.auth import views
from .forms import UserLoginForm, ChangePasswordForm
from user.views import SignUpView, UserDetailView, UserListView
urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path(
        'login/',
        views.LoginView.as_view(
            template_name="accounts/login.html",
            authentication_form=UserLoginForm
        ),
        name='login'
    ),
    path(
        'password_change/', views.PasswordChangeView.as_view(
            template_name='accounts/password_change_form.html',
            form_class=ChangePasswordForm,
        ), name='change_password'),
    path('std_profile/<int:pk>/', UserDetailView.as_view(), name="std_profile"),
    path('all_users/', UserListView.as_view(), name="user_list"),
]