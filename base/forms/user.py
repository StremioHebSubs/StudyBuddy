from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from base.models import User


class UserRegistrationForm(UserCreationForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Dwayne Johnson'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'The Rock'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'DwayneJohnson@gmail.com'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '********'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '********'}))
    
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']


class UserLoginForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'DwayneJohnson@gmail.com'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '********'}))

    class Meta:
        model = User
        fields = ['email', 'password']

    def validateLogin(self, request):
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


class UserUpdateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Dwayne Johnson'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'The Rock'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'DwayneJohnson@gmail.com'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'I am a professional wrestler and actor'}))

    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'bio', 'avatar']
