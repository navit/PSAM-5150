from django import forms

#from russia.models import Signup
from russia.models import ContactDetails


class ContactDetailsForm(forms.ModelForm):

	class Meta:
		model = ContactDetails
		fields = ['name', 'email', 'street_address', 'city', 'zipcode', 'country', 'question']

