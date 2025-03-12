from django import forms
from .models import RegisterUser

class RegisterUserForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        ),
        label="Senha"
    )

    class Meta:
        model = RegisterUser
        fields = [
            'fullname', 
            'email', 
            'password'
        ]

class LoginForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={'class': 'form-control'}
        )
    )
    password = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )     
    )




