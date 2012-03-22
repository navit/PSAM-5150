from django.db import models


GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
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
EMPLOYMENT_STATUS_CHOICES =(
    ('EM', 'Employed'),
    ('UD', 'Under Employed'),
    ('UN', 'Un Employed'),

    )
    

class CensusInfo(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=3, choices=GENDER_CHOICES)
    marital_status = models.CharField(max_length=3, choices=MARITAL_CHOICES)
    education = models.CharField(max_length=3, choices=YEAR_IN_SCHOOL_CHOICES)
    employment_status = models.CharField(max_length=3, choices=EMPLOYMENT_STATUS_CHOICES)
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


