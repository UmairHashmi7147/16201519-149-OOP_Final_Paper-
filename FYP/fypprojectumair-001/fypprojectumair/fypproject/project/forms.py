from django import forms
from .models import Job,intoresume
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class loginForm(forms.ModelForm):
    class Meta:
       # model=User
        fields=['uname','em','pas','rad']


class job_data_insertion(forms.ModelForm):
    class Meta:
        model=Job
        fields=['job_title','job_description','job_skills','job_skills_periority','job_career_level','job_career_level_periority','job_positions','job_country','job_degree_level','job_degree_level_periority','job_min_experience','job_experience_periority','job_min_sallery','job_max_sallery','job_prefrence','job_prefrence_periority']


class resume_data_into_databse(forms.ModelForm):
    class Meta:
        model=intoresume
        fields=['d_resume_title','d_resume_name','d_resume_email','d_resume_cnic','d_resume_contact','d_resume_gender','d_resume_region','d_resume_career_level','d_resume_degreelevel','d_resume_subdegreelevel','d_resume_skills','d_resume_experience']

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username','email','password1','password2']

