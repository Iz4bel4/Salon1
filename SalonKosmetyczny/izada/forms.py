from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm 
from django import forms
from django.contrib.auth.models import User
from .models import *
#TODO: przesyłanie formularza/ czy wysylanie emaili bedzie tutaj?

# class OfferForm(forms.ModelForm):
#      class Meta:
#          model = Offer
#          fields = ('offer_name','offer_price')