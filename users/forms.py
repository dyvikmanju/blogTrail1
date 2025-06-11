from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    image = forms.ImageField(
        required=False,
        label="Update Profile Pic",  # ✅ Custom label
        widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
    )

    class Meta:
        model = Profile
        fields = ['image']
