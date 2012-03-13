from django.contrib import admin
from russia.models import  ContactDetails 



class ContactDetailsAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_on'
    list_display = ('email', 'created_on', 'is_accepted',)
    list_filter = ('is_accepted',)
    list_display_links = ('email',)
    search_fields = ['email', 'name', 'admin_comments', 'street_address', 'city', 'zipcode', 'country', 'question', ]

admin.site.register(ContactDetails, ContactDetailsAdmin)

