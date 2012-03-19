from django.db import models


GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    )

YEAR_IN_SCHOOL_CHOICES = (
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
    ('GR', 'Graduate'),
)

MARITAL_CHOICES = (
    ('SG', 'Single'),
    ('DV', 'Divorced'),
    ('MR', 'Married'),
    ('WI', 'Widowed'),

    )
    

class CensusInfo(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    marital_status = models.CharField(max_length=1, choices=MARITAL_CHOICES)
    education = models.CharField(max_length=1, choices=YEAR_IN_SCHOOL_CHOICES)
    email = models.EmailField()
    phone = models.PositiveIntegerField(max_length=100)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)
    country = models.CharField(max_length=10)
    is_accepted = models.BooleanField(default=False)
    admin_comments = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name


