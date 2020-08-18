import os
import re
from django.contrib.auth.admin import UserAdmin
import nltk
from django.contrib.auth.decorators import login_required
from array import array
import datetime
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
import PyPDF2
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404,redirect
from django.conf import settings
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from .forms import loginForm, job_data_insertion, resume_data_into_databse,UserRegisterForm
from django.core.mail import send_mail
from .models import Patient,Department
import string
import random
from django.utils.crypto import get_random_string
from textblob import TextBlob
from .utils import render_to_pdf
from django.http import HttpResponse
from django.template.loader import get_template





def gohome(request):
    return render(request,'final.html')


def viewdata(request):
    obj=Patient.objects.all()
    param={'param':obj}
    return render(request,'viewdata.html',param)

def insertdata(request):
    if request.method == 'POST':
        pname=request.POST.get('pname')
        fname=request.POST.get('fname')
        phone=int(request.POST.get('phone'))
        age=int(request.POST.get('age'))
        gender=request.POST.get('gender')
        cnic=request.POST.get('cnic')
        address=request.POST.get('address')
        disease=request.POST.get('disease')
        obj=Patient.objects.create(Pid=1,Pname=pname,PFathername=fname,Pphone=phone,Page=age,Pgender=gender,Pcnic=cnic,Paddress=address,Pdisease=disease)
        obj.save()
        obj1 = Patient.objects.filter(Pname=pname,PFathername=fname,Pphone=phone,Page=age,Pgender=gender,Pcnic=cnic,Paddress=address,Pdisease=disease)
        obj1.update(Pid=obj.id,slug=obj.id)

    return render(request,'insertdata.html')


def delpatient(request,slug):
    if (slug!=""):

        obj=Patient.objects.filter(slug=slug)
        obj.delete()
        return redirect('/viewdata/')
    return render(request,'viewdata.html')


def refer(request,slug):
    if (slug!=""):
        param={'param':slug}
        return render(request, 'refer.html',param)
    return render(request,'viewdata.html')

def refered(request):
    slug = request.POST.get('slug')
    department = request.POST.get('department')
    dname = request.POST.get('dname')
    obj=Department.objects.filter(slug=slug)
    if(obj.count()==0):
        Pid=0
        obj1=Patient.objects.filter(slug=slug)
        for data in obj1:
            Pid=data.Pid
        obj2=Department.objects.create(Pid_id=Pid,Dname=dname,Dtype=department)
        obj2.save()
        obj3=Department.objects.filter(Pid_id=Pid,Dname=dname,Dtype=department)
        obj3.update(slug=obj2.id)
    else:
        error="Department Alread Refered...! "
        obj4=Patient.objects.all()
        param={'error':error,
               'param':obj4}
        return render(request, 'viewdata.html',param)
    return render(request,'viewdata.html')

def updatedata(request):
    obj=Patient.objects.all()
    param={
        'param':obj
    }
    if request.method == 'POST':
        Pid=request.POST.get("id")
        Pname=request.POST.get("pname")
        Pdisease=request.POST.get("disease")
        obj=Patient.objects.filter(Pid=Pid)
        obj.update(Pname=Pname,Pdisease=Pdisease)
        obj = Patient.objects.all()
        param = {
            'param': obj
        }
        return render(request, 'updatedata.html', param)
    return render(request,'updatedata.html',param)

