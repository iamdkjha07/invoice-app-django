from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class ServiceProviderForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['client', 'company_name', 'handle_by', 'email', 'phone',
                  'account_number', 'ifsc_code', 'bank_name', 'gst_number']