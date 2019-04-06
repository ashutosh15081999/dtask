from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Comments

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',]

# class UserUpdateForm(forms.ModelForm):
#     email = forms.EmailField()
#     class Meta:
#         model = User
#         fields = ['username', 'email']


# class ProfileUpdateForm(forms.ModelForm):
#     #image = forms.ImageField()
#     class Meta:
#         model = Profile
#         fields = ['image']


# class ProfileForm(UserCreationForm):
    

#     class Meta:
#         model = Profile
#         fields = ['MyNickNames','image', 'contact_no','AboutMe']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['contact_no','about_me','nick_names','image','frequently_uttered_words','striking_features']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']