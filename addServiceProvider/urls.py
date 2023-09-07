from django.urls import path
from addServiceProvider import views

urlpatterns = [
    path('', views.addServiceProviderDetails, name='addServiceProviderDetails'),
    path('update_company/<int:id>', views.update_company , name='update_company'),
    path('delete_company/<int:id>/', views.delete_company, name='delete_company'),
]