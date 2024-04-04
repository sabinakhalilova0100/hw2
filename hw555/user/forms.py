from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(required=True, min_length=4, max_length=20,
                               widget=forms.TextInput({'class': 'form-control', 'type': 'text'}))
    password = forms.CharField(min_length=8, max_length=20,
                               widget=forms.PasswordInput({'class': 'form-control', 'type': 'password'}))


class RegisterForm(forms.ModelForm):
    repeat_password = forms.CharField(required=True, min_length=8, max_length=20,
                                      widget=forms.PasswordInput({'class': 'form-control', 'type': 'password',
                                                                  'placeholder': 'Please repeat your password'}))
class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your last name'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
        }


def clean_repeat_password(self):
    password1 = self.cleaned_data.get("password")
    password2 = self.cleaned_data.get("repeat_password")
    if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
    return password2


def save(self, commit=True):
    user = super().save(commit=False)
    user.set_password(self.cleaned_data["password"])
    if commit:
        user.save()
        return user
