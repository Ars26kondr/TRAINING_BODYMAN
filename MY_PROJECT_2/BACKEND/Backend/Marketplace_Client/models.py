from django.db import models
from django.contrib.auth.models import AbstractUser
class Customer(AbstractUser):
    surname=models.CharField(max_length=50, null=True, blank=True)
    given_name=models.CharField(max_length=30, null=True, blank=True)
    email=models.EmailField()
    date=models.DateField(null=True, blank=True)
    phone_number=models.CharField(max_length=16, null=True, blank=True)
    province=models.CharField(max_length=100, null=True, blank=True)
    country=models.CharField(max_length=50, null=True, blank=True)
    address=models.CharField(max_length=50, null=True, blank=True)