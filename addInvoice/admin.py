from django.contrib import admin
from addInvoice.models import Client, Services

# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'company_name', 'gst_number', 'country', 'state', 'created_at']
    search_fields = ['company_name', 'gst_number', 'state', 'country']

admin.site.register(Client, ClientAdmin)



class ServicesAdmin(admin.ModelAdmin):
    list_display = ['id', 'client', 'description', 'quantity', 'amount', 'created_at']
    search_fields = ['client', 'description', 'quantity', 'amount']

admin.site.register(Services, ServicesAdmin)