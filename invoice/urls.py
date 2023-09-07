from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('add-invoice/', include('addInvoice.urls')),
    path('add-service-provider/', include('addServiceProvider.urls')),
    path('review-invoice/', include('reviewInvoice.urls')),
    path('invoice-report/', include('invoiceReport.urls')),
]
