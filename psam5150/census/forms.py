# -*- coding: UTF-8 -*-
from django import forms
from census.models import CensusInfo


class CensusInfoForm(forms.ModelForm):
 
  class Meta:
    model = CensusInfo
    fields = ['name', 'gender', 'marital_status', 'employment_status', 'education', 'email', 'phone', 'street_address', 'city', 'zipcode','country']

