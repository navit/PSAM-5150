# -*- coding: UTF-8 -*-
from django.contrib import admin
from census.models import CensusInfo


class CensusInfoAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_on'
    list_display = ('email', 'created_on', 'is_accepted',)
    list_filter = ('is_accepted',)
    list_display_links = ('email',)
    search_fields = ['name', 'email', 'phone', 'gender', 'street_address','employment_status', 'city', 'zipcode','country', ]




admin.site.register(CensusInfo, CensusInfoAdmin)

