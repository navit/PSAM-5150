from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.sites.models import get_current_site
from django.shortcuts import redirect
from django.contrib import messages

from census.forms import CensusInfoForm
from census.models import  CensusInfo


def home(request):
    return render_to_response('home.html', context_instance=RequestContext(request))


def censusinfophome(request):
    oursite = get_current_site(request)
    return render_to_response('censustemp/main.html', {'title': oursite.name}, context_instance=RequestContext(request))


def sitecensusinfo(request):
    if request.method == 'POST':
        form = CensusInfoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "Your form has been submitted and will be processed in the order it was received")
            return redirect('censusresults')
    else:
        form = CensusInfoForm()
    return render_to_response('censustemp/censusinfo.html', {'form': form}, context_instance=RequestContext(request))


def censusresults(request):
    peoplecount = len(CensusInfo.objects.all())
    return render_to_response('censustemp/results.html', {'people': peoplecount,})


