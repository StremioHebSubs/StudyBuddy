"""
User Forms for StudyBuddy

This module defines various user-related forms used in the StudyBuddy Base application.
The forms include registration, login, and profile update forms for users.

The forms are designed to capture user information such as name, email, username, and password.
They also include features like password validation and placeholders for input fields.

For more information on creating forms with Django, refer to the Django documentation:
https://docs.djangoproject.com/en/stable/topics/forms/
"""
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from base.models import User


class UserRegistrationForm(UserCreationForm):
    """
    User Registration Form

    This module defines a form for user registration in the StudyBuddy Base application.
    The form captures user information such as name, username, email, and password.
    It includes password validation and placeholders for input fields.
    """
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Dwayne Johnson'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'The Rock'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'DwayneJohnson@gmail.com'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '********'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '********'}))
    
    class Meta:
        """
        Meta Configuration for User Registration Form

        The 'Meta' class provides configuration options for the 'UserRegistrationForm.'
        It specifies the model associated with the form and the fields to include in the form.
        """
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']


class UserLoginForm(forms.ModelForm):
    """
    User Login Form

    This module defines a form for user login in the StudyBuddy Base application.
    The form allows users to log in using their email and password.
    It includes placeholders for input fields and provides login validation.
    """
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'DwayneJohnson@gmail.com'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '********'}))

    def validateLogin(self, request) -> User:
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user is None:
            if not User.objects.filter(email=email).exists():
                self.add_error('email', "Email doesn't exist")

            else:
                self.errors.clear()
                self.add_error('password', "Password doesn't match")

        return user
    
    class Meta:
        """
        Meta Configuration for User Login Form

        The 'Meta' class provides configuration options for the 'UserLoginForm.'
        It specifies the model associated with the form and the fields to include in the form.
        """
        model = User
        fields = ['email', 'password']


class UserUpdateForm(forms.ModelForm):
    """
    User Profile Update Form

    This module defines a form for updating user profiles in the StudyBuddy Base application.
    Users can modify their name, username, email, bio, and avatar using this form.
    It includes placeholders for input fields and allows users to update their profile.
    """
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Dwayne Johnson'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'The Rock'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'DwayneJohnson@gmail.com'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'I am a professional wrestler and actor'}))

    class Meta:
        """
        Meta Configuration for User Profile Update Form

        The 'Meta' class provides configuration options for the 'UserUpdateForm.'
        It specifies the model associated with the form and the fields to include in the form.
        """
        model = User
        fields = ['name', 'username', 'email', 'bio', 'avatar']
