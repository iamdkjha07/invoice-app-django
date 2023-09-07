from django.urls import path
from authentication.views import *

urlpatterns = [
    path('', loginPage, name='loginPage'),
    path('signup/', signupPage, name='signupPage')
]
