from django.urls import path
from dashboard.views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('logOut', logOut, name='logOut'),
]
