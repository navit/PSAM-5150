from django import forms

from russia.models import Signup
from russia.models import ContactDetails


class HelloWorldForm(forms.Form):
    name = forms.CharField(max_length=100)
    location = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)

class SignupForm(forms.ModelForm):

    class Meta:
        model = Signup
        fields = ['name', 'email', 'reason_for_joining', 'url']

class ContactDetailsForm(forms.ModelForm):

	class Meta:
		model = ContactDetails
		fields = ['name', 'email', 'street_address', 'city', 'zipcode', 'country','question']

