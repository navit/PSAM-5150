from django.contrib import admin
from russia.models import Signup, ContactDetails

#class HelloWorldAdmin(admin.ModelAdmin):
 # date_hierarchy = 'created_on'
 # list_display = ('created_on', 'name', 'location', )

class SignupAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_on'
    list_display = ('email', 'created_on', 'is_accepted', 'url',)
    list_filter = ('is_accepted',)
    list_display_links = ('email',)
    search_fields = ['email', 'name', 'admin_comments', 'url','reason_for_joining', ]


class ContactDetailsAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_on'
    list_display = ('email', 'created_on', 'is_accepted',)
    list_filter = ('is_accepted',)
    list_display_links = ('email',)
    search_fields = ['email', 'name', 'admin_comments', 'street_address', 'city', 'zipcode', 'country', 'question', ]



#admin.site.register(HelloWorld, HelloWorldAdmin)
admin.site.register(Signup, SignupAdmin)
admin.site.register(ContactDetails, ContactDetailsAdmin)

