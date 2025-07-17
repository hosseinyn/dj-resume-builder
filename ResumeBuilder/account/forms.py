from django.contrib.auth.forms import UserCreationForm , AuthenticationForm , PasswordChangeForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class" : "auth-input"}) , label="Username ")

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class" : "auth-input"}) , label="Password ")

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class" : "auth-input"}) , label="Confirm Password ")

    class Meta:
        model = User
        fields=["username" , "password1" , "password2"]


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class" : "auth-input"}) , label="Username ")

    password = forms.CharField(widget=forms.PasswordInput(attrs={"class" : "auth-input"}) , label="Password ")

    class Meta:
        model = User
        fields=["username" , "password"]

class ChangePasswordForm(PasswordChangeForm):

    class Meta:
        model = User
        fields=["old_password" , "new_password1" , "new_password2"]