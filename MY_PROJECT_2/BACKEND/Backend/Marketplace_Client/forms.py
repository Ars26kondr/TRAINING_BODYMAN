from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Customer
class Customer_Registration_form(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=Customer
        fields=('surname','given_name','email','date',
                'phone_number','province','country','address')