# -*- coding: UTF-8 -*-
from django.contrib import admin
from census.models import CensusInfo
#from census.models import Choice

class CensusInfoAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_on'
    list_display = ('email', 'created_on', 'is_accepted',)
    list_filter = ('is_accepted',)
    list_display_links = ('email',)
    search_fields = ['name', 'email', 'phone', 'street_address', 'city', 'zipcode','country', ]


#class ChoiceAdmin(admin.ModelAdmin):
  #  list_display = ('gender', )
   # search_fields = ['gender',]

admin.site.register(CensusInfo, CensusInfoAdmin)
#admin.site.register(Choice, ChoiceAdmin)

