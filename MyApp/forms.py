from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import OrderPlacement

class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class OrderPlacementForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)
    retype_password = forms.CharField(max_length=200)

    class Meta:
        model=OrderPlacement
        fields = ("first_name", "last_name", "email", "username", "password", "retype_password")

