from django.urls import path
from reviewInvoice.views import *

urlpatterns = [
    path('all-client-details/', allClientDetails, name='allClientDetails'),
    path('all-client-details/<int:pk>', showReview, name='showReview'),
]
