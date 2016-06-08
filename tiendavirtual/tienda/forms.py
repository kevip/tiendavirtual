from django import forms
from django.contrib.auth.models import User

class RegUsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password"]
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'validate',
                       'required': True},
            ),
            'last_name': forms.TextInput(
                attrs={'class': 'validate',
                       'required': True}
            ),
            'email': forms.EmailInput(
                attrs={'class': 'validate',
                       'required': True}
            ),
            'password': forms.PasswordInput(
                attrs={'class': 'validate',
                       'required': True}
            ),
        }
