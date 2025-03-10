from django import forms
from .models import RegisterUser

class RegisterUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = RegisterUser
        fields = [
            'fullname',
            'email',
            'password'
        ]

    def clear_email(self):
        email = self.cleaned_data.get('email')

        if RegisterUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Este e-mail já está cadastrado.")
        else:
            return email