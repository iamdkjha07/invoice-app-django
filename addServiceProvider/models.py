from django.db import models
from addInvoice.models import *

# Create your models here.
class Company(models.Model):
    client = models.OneToOneField(
        Client, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=250)
    handle_by = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    phone = models.BigIntegerField()
    account_number = models.BigIntegerField()
    ifsc_code = models.CharField(max_length=250)
    bank_name = models.CharField(max_length=250)
    gst_number = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.company_name} - 'client: '{self.client}"