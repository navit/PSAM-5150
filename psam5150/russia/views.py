from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.sites.models import get_current_site
from django.shortcuts import redirect
from django.contrib import messages

from russia.forms import ContactDetailsForm


def home(request):
    return render_to_response('home.html', context_instance=RequestContext(request))


def signuphome(request):
    oursite = get_current_site(request)
    return render_to_response('signup/main.html', {'title': oursite.name}, context_instance=RequestContext(request))


def sitecontactdetails(request):
    if request.method == 'POST':
        form = ContactDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "Your form has been submitted and will be processed in the order it was received")
            return redirect('signup_main')
    else:
        form = ContactDetailsForm()
    return render_to_response('signup/contactdetails.html', {'form': form}, context_instance=RequestContext(request))


