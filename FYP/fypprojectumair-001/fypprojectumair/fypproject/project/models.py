from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse
from django.template.defaultfilters import slugify
from django.utils import timezone


Deparment_Choices = (
    ('M', 'Medical'),
    ('S', 'Surgicsal'),
    ('O', 'OTP'),
    ('I', 'ICU'),
    ('IT', 'ITC'),
)


class Patient(models.Model):
    Pid=models.IntegerField(max_length=15,blank=False)
    Pname = models.CharField(max_length=15,blank=True)
    PFathername = models.CharField(max_length=15,blank=True)
    Pphone=models.IntegerField(max_length=15,blank=False)
    Page = models.IntegerField(blank=False)
    Pgender = models.CharField(max_length=15, blank=False)
    Pcnic = models.CharField(max_length=15, blank=False)
    Paddress=models.CharField(max_length=45,blank=True)
    Pdisease=models.CharField(max_length=35,blank=True)
    active=models.BooleanField(default=True)
    modified_when=models.DateField(default=timezone.now)
    slug = models.SlugField(null=True, blank=True)
    def __str__(self):
        return self.Pname

    def get_absolute_urls(self):
        return reverse('delpatient', kwargs={'slug': self.slug})

    def get_refer_urls(self):
        return reverse('refer', kwargs={'slug': self.slug})


class Department(models.Model):
    Pid=models.ForeignKey(Patient,on_delete=models.CASCADE)
    Dname = models.CharField(max_length=15,blank=True)
    Dtype = models.CharField(choices=Deparment_Choices,max_length=6,blank=True)
    No_of_employees=models.IntegerField(default=100)
    No_of_beds = models.IntegerField(default=50)
    No_of_patients = models.IntegerField(default=0)
    slug = models.SlugField(null=True, blank=True)
    def __str__(self):
        return self.pname




