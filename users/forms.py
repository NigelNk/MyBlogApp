from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms.models import ModelForm

from users.models import UserAccount, UserProfile


class UserAccountCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model   = UserAccount
        fields  = ('username', 'email')


class UserAccountChangeForm(UserChangeForm):
    class Meta:
        model = UserAccount
        fields = ('username', 'email')

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            "first_name",
            "last_name",
            "image_url",
            "short_bio",
            "long_bio",
            "facebook",
            "twitter",
            "linkedin",
        ]
