from django.urls import path
from invoiceReport.views import *

urlpatterns = [
    path('', invoiceReport, name='invoiceReport'),
    path('gst-report/<int:pk>', gstReport, name='gstReport'),
]
