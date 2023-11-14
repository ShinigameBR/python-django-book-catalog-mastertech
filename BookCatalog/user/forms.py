from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'text_box', 'placeholder': 'Usuário'}), label='')
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': ' text_box', 'id': 'password1', 'placeholder': 'Senha'}), label='')
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': ' text_box', 'id': 'password2', 'placeholder': 'Confirmar Senha'}), label='')

    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + \
            ('first_name', 'last_name',  'email',
             'img', 'password1', 'password2')

        help_texts = {
             'email': 'IMAGEM PARA PERFIL (OPCIONAL)',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'name text_box',
                'placeholder': 'Nome',
                'id': 'username'}),

            'last_name': forms.TextInput(attrs={
                'class': 'name text_box',
                'placeholder': 'Sobrenome',
                'id': 'username'}),

            'email': forms.EmailInput(attrs={
                'class': 'email text_box',
                'placeholder': 'Email',
                'id': 'username'}),

            'img': forms.FileInput(attrs={
                'class': 'email text_box',
                'id': 'username'}),
        }

        labels = {
            'username': '',
            'first_name': '',
            'last_name': '',
            'email': '',
            'password1': '',
            'password2': '',
            'img': '',


        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'img')


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'username text_box', 'placeholder': 'Usuário', 'id': 'username'}), label='')
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'pass text_box',
            'placeholder': 'Senha',
            'id': 'password',

        }
    ), label='')


class ChangePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)

    old_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'pass text_box', 'placeholder': 'Old Password', 'id': 'username'}), label='')
    new_password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'pass text_box',
            'placeholder': 'Nova Senha',
            'id': 'New_Password1',

        }
    ), label='')
    new_password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'pass text_box',
            'placeholder': 'Confirmar Nova Senha',
            'id': 'New_Password2',
        }
    ), label='')