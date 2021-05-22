from django import forms
from captcha.fields import CaptchaField

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from simplemathcaptcha.fields import MathCaptchaField



class NewUserForm(UserCreationForm):

    captcha = MathCaptchaField()

    class Meta:
        model=User
        fields = ("username", "password1", "password2")



