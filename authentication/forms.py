from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class UserLogin(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

        # labels = {
        #     'username' : 'UserId',
        #     'password' : 'Password'
        # }

        # widgets = {
        #     "username" : forms.TextInput(attrs={'placeholder':'username'}),
        # }

        

        