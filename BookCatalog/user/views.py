from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from .forms import CustomUserCreationForm
from user.models import CustomUser
from django.views import generic
from.models import CustomUser
# Create your views here.

class UserListView(ListView):
    model = CustomUser
    template_name = "user/home.html"
    context_object_name = 'users'


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm

    success_url = reverse_lazy('login')

    template_name = "accounts/signup.html"


class UserDetailView(DetailView):
    model = CustomUser
    template_name = "user/profile.html"
    context_object_name = 'user'