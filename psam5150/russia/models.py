from django.db import models

class HelloWorld(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    message = models.TextField()

    def __unicode__(self):
        return self.name

class Signup(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    reason_for_joining = models.TextField()
    #picture = models.ImageField(upload_to='signupform/pics/')
    url = models.URLField(verify_exists=True)
    is_accepted = models.BooleanField(default=False)
    admin_comments = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name

class ContactDetails(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)
    country = models.CharField(max_length=10)
    question = models.TextField(max_length=400)
    is_accepted = models.BooleanField(default=False)
    admin_comments = models.TextField(blank=True, null=True) #

    def __unicode__(self):
        return self.name


# def save method this method calls the save method of the super class.  we call it here to proparly save. we are overriding the defalut
# save method. 



