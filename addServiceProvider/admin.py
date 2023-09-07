from django.contrib import admin
from addServiceProvider.models import *

# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'client', 'company_name', 'handle_by', 'email', 'phone', 'created_at']
    search_fields = ['client', 'company_name', 'handle_by', 'email', 'phone']

admin.site.register(Company, CompanyAdmin)