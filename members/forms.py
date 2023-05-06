from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    address = forms.CharField(max_length=250)

    class Meta:
        model = User
        fields = ('username', 'email', 'birth_date', 'address', 'password1', 'password2',)
