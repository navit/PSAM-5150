from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.sites.models import get_current_site
from django.shortcuts import redirect
from django.contrib import messages

from census.forms import CensusInfoForm
#from census.forms import ChoiceForm


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
            return redirect('censustemp_main')
    else:
        form = CensusInfoForm()
    return render_to_response('censustemp/censusinfo.html', {'form': form}, context_instance=RequestContext(request))


#def sitechoice(request):
  #  if request.method == 'POST':
   #     form = ChoiceForm(request.POST, request.FILES)
    #    if form.is_valid():
   #         form.save()
      #      messages.add_message(request, messages.INFO, "Your form has been submitted and will be processed in the order it was received")
       #     return redirect('censustemp_main')
  #  else:
   #     form = ChoiceForm()
  #  return render_to_response('censustemp/choice.html', {'form': form}, context_instance=RequestContext(request))



