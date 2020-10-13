from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.forms import ModelForm

from twitter.models import Tweet


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")
        fields_classes = {'username': UsernameField}


class TweetForm(ModelForm):
    class Meta:
        model = Tweet
        exclude = ["created_date", "author", "likes"]
