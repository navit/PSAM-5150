from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.core.urlresolvers import reverse

from forms import AppointmentModelForm
from models import Contacts, EventType


class WelcomePage(TemplateView):
    template_name = 'appointments/welcome.html'


class BookAnAppointment(CreateView):
    form_class = AppointmentModelForm
    template_name = 'appointments/form.html'


    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, message="Your submission is complete")
        return reverse('appointments_welcome_page')
        #super(BookAnAppointment, self).get_success_url()


class AddContact(CreateView):
    model = Contacts
    template_name = 'appointments/form.html'

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, message="Your contact has been added")
        return reverse('appointment_welcome_page')
        #super(AddContact, self).get_success_url()

class AddEventType(CreateView):
    model = EventType
    template_name = 'appointments/form.html'

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, message="Your Event Type has been added")
        return reverse('appointment_welcome_page')
        #super(AddEventType, self).get_success_url()
