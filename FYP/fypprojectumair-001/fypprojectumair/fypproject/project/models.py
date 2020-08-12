from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse
from django.template.defaultfilters import slugify
from django.utils import timezone


CHOICES = (
    ('J', 'Job Seeker'),
    ('O', 'Organization'),
)

class Type(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    type = models.CharField(choices=CHOICES,max_length=1,blank=True)
    emcon=models.CharField(max_length=15,blank=False)
    con=models.BooleanField(default=False)



class Job(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        job_id = models.AutoField
        job_title = models.CharField(max_length=20)
        job_description = models.CharField(max_length=50)
        job_skills = models.CharField(max_length=50)
        job_skills_periority=models.IntegerField()
        job_career_level = models.CharField(max_length=50)
        job_career_level_periority = models.IntegerField()
        job_positions = models.IntegerField()
        job_country = models.CharField(max_length=50)
        job_degree_level = models.CharField(max_length=50)
        job_degree_level_periority = models.IntegerField()
        job_min_experience = models.CharField(max_length=20)
        #job_max_experience = models.CharField(max_length=20)
        job_experience_periority = models.IntegerField()
        job_min_sallery = models.IntegerField()
        job_max_sallery = models.IntegerField()
        job_prefrence = models.CharField(max_length=20)
        job_prefrence_periority = models.IntegerField()
        recommend_request=models.BooleanField(default=False)
        request_status=models.CharField(max_length=50, blank=True, null=True)
        slug = models.SlugField(null=True, blank=True)  # new



        def get_absolute_urls(self):
            return reverse('deljob', kwargs={'slug': self.slug})
        def get_job_accept_urls(self):
            return reverse('acceptjob', kwargs={'slug': self.slug})
        def get_job_data_urls(self):
            return reverse('viewjob', kwargs={'slug': self.slug})
        def get_recommend_urls(self):
            return reverse('job_data_get', kwargs={'slug': self.slug})
        def get_request_urls(self):
            return  reverse('recommendrequest')

        


class intoresume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    d_resume_id=models.AutoField
    d_resume_title=models.CharField(max_length=50)
    d_resume_name=models.CharField(max_length=30)
    d_resume_email=models.CharField(max_length=30)
    d_resume_dob=models.DateField(max_length=30 , null=True, blank=True)
    #d_resume_contact = models.CharField(max_length=30, null=True, blank=True)
    d_resume_contact=models.CharField(max_length=30 , default="03165009006")
    d_resume_cnic=models.CharField(max_length=30)
    d_resume_gender=models.CharField(max_length=10)
    d_resume_region=models.CharField(max_length=20)
    d_resume_career_level=models.CharField(max_length=50)
    d_resume_degreelevel=models.CharField(max_length=20)
    d_resume_subdegreelevel=models.CharField(max_length=20)
    d_resume_skills=models.CharField(max_length=1000)
    d_resume_experience=models.CharField(max_length=20)
    d_resume_description=models.CharField(max_length=500 , null=True, blank=True)
    d_resume_profile=models.ImageField(null=True,blank=True)
    d_resume_counter=models.IntegerField( default=0)
    d_resume_status=models.BooleanField(default=True)
    slug = models.SlugField(null=True, blank=True)  # new

    def __str__(self):
        return self.d_resume_name




class recommended(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    d_resume_id = models.AutoField
    d_resume_title = models.CharField(max_length=50)
    d_resume_name = models.CharField(max_length=30)
    d_resume_email = models.CharField(max_length=30)
    d_resume_cnic = models.CharField(max_length=30)
    d_resume_gender = models.CharField(max_length=10)
    d_resume_region = models.CharField(max_length=20)
    d_resume_career_level = models.CharField(max_length=50)
    d_resume_degreelevel = models.CharField(max_length=20)
    d_resume_subdegreelevel = models.CharField(max_length=20)
    d_resume_skills = models.CharField(max_length=50)
    d_resume_experience = models.CharField(max_length=20)
    d_resume_counter = models.IntegerField( default=0)
    forjob=models.CharField(max_length=10,null=True,blank=True)
    calforinter=models.BooleanField(default=False)
    hired=models.BooleanField(default=False)
    slug = models.SlugField(null=True, blank=True)  # new

    def __str__(self):
        return self.d_resume_name

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})
    def get_call_url(self):
        return reverse('call_for_interview', kwargs={'slug': self.slug})
    def get_hire_url(self):
        return reverse('hired', kwargs={'slug': self.slug})

    def get_del_url(self):
        return reverse('delrecommended', kwargs={'slug': self.slug})
    def get_delcallforinterview_url(self):
        return reverse('delcallforinterview', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.d_resume_cnic)
        return super().save(*args, **kwargs)




class messeges(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    msgfrom=models.IntegerField
    msgto=models.IntegerField
    msg=models.CharField(max_length=500,blank=True)
    slug = models.SlugField(null=True, blank=True)
    def __str__(self):
        return self.id



#class DeleteModel(User):
class FeedBack(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    subject=models.CharField(max_length=30)
    disc=models.TextField(max_length=1000)
    feedback_date=models.DateField(default=timezone.now)
    response=models.TextField(max_length=500,blank=True,null=True,default="No Response Yet")
    slug = models.SlugField(null=True, blank=True)  # new

    def __str__(self):
        return self.subject

    def get_absolute_urls(self):
        return reverse('delfeedback', kwargs={'slug': self.slug})

    '''def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.validate_unique())
        return super().save(*args, **kwargs)'''



class contactdbs(models.Model):
    id=models.AutoField(auto_created = True, primary_key = True)
    name=models.CharField(max_length=300 , default="xyz")
    email=models.CharField(max_length=300,default="xyz")
    subject=models.CharField(max_length=300,default="xyz")
    message=models.CharField(max_length=300,default="ffffff")

    def __str__(self):
        return self.email





