from django import forms
from django.contrib.auth.forms import UserCreationForm
from User.models import CustomUser


class SigninForm(forms.Form):
    email = forms.EmailField(max_length=45, required=True)
    password = forms.CharField(min_length=6, widget=forms.PasswordInput)


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("email", 'username',)
