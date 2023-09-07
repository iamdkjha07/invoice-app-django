from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['company_name', 'gst_number', 'country', 'state', 'address']



class ServicesForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = ['client', 'description', 'quantity', 'amount']









