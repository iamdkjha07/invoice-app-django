from django.urls import path
from addInvoice import views

urlpatterns = [
    path('add-client-details/', views.addInvoice, name='addInvoice'),
    path('add-services/',views.addInvoice2, name='addInvoice2'),
]
