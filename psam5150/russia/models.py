from django.db import models


class ContactDetails(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)
    country = models.CharField(max_length=10)
    #url = models.URLField(verify_exists=True)
    question = models.TextField(max_length=400)
    is_accepted = models.BooleanField(default=False)
    admin_comments = models.TextField(blank=True, null=True) 

    def __unicode__(self):
        return self.name





