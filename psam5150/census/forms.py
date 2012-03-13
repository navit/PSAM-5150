# -*- coding: UTF-8 -*-
from django import forms
from census.models import CensusInfo



class CensusInfoForm(forms.ModelForm):
 
  class Meta:
    model = CensusInfo
    fields = ['name', 'email', 'phone', 'street_address', 'city', 'zipcode','country']

