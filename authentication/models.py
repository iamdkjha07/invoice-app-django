from django.db import models

# Create your models here.
class UserSignUp(models.Model):
    fullName = models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    phoneNumber = models.BigIntegerField()
    emailId = models.EmailField()
    userpass1 = models.CharField(max_length=150)
    userpass2 = models.CharField(max_length=150)