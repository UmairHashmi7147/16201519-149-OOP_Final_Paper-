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
from .models import Job, intoresume, recommended, User, Type, FeedBack, contactdbs,messeges
import string
import random
from django.utils.crypto import get_random_string
from textblob import TextBlob
from .utils import render_to_pdf
from django.http import HttpResponse
from django.template.loader import get_template


class var:
    global uname, pas, em, rad, randnum

    def __init__(self, uname='', pas='', em='', rad='', randnum=''):
        self.uname = uname
        self.pas = pas
        self.em = em
        self.rad = rad
        self.randnum = randnum

    def getuname(self):
        return self.uname

    def getpas(self):
        return self.pas

    def getem(self):
        return self.em

    def getrad(self):
        return self.rad

    def getrandnum(self):
        return self.randnum

    def setuname(self, a):
        self.uname = a

    def setpas(self, a):
        self.pas = a

    def setem(self, a):
        self.em = a

    def setrad(self, a):
        self.rad = a

    def setrandnum(self, a):
        self.randnum = a


object = var()

@login_required
def goprofile(request):
    user=request.user
    if(request.user.is_superuser):
        sub = ""
        disc = ""
        text = ""
        polarity = 0
        positive = 0
        wpositive = 0
        spositive = 0
        negative = 0
        wnegative = 0
        snegative = 0
        neutral = 0
        try:
            obj = FeedBack.objects.all()
            for data in obj:
                text = TextBlob(data.subject + " " + data.disc)
                print(text)
                polarity += text.sentiment.polarity
                if (text.sentiment.polarity == 0):  # adding reaction of how people are reacting to find average later
                    neutral += 1
                elif (text.sentiment.polarity > 0 and text.sentiment.polarity <= 0.3):
                    wpositive += 1
                elif (text.sentiment.polarity > 0.3 and text.sentiment.polarity <= 0.6):
                    positive += 1
                elif (text.sentiment.polarity > 0.6 and text.sentiment.polarity <= 1):
                    spositive += 1
                elif (text.sentiment.polarity > -0.3 and text.sentiment.polarity <= 0):
                    wnegative += 1
                elif (text.sentiment.polarity > -0.6 and text.sentiment.polarity <= -0.3):
                    negative += 1
                elif (text.sentiment.polarity > -1 and text.sentiment.polarity <= -0.6):
                    snegative += 1
            # print('polarity',polarity,'positive',positive,'wpositive',wpositive,'spositive',spositive,'wnegative',wnegative,'negative',negative,'snegative',snegative)
            param = {
                'pol': str(polarity),
                'net': neutral,
                'wpos': wpositive,
                'pos': positive,
                'spos': spositive,
                'neg': negative,
                'sneg': snegative,
                'wneg': wnegative, }
            print(wnegative, polarity)
            return render(request, 'admin.html', param)
        except:
            print("hahaha")
        return render(request, 'admin.html')

    obj=Type.objects.get(user_id=user.id)
    if (obj.con == True):
        #login(request, user)
        print(user.username)
        if(obj.type== 'O'):
            try:
             print("hahahah1")
             obj=Job.objects.filter(user_id=user.id)

             # for y in obj:
             #     if (y.job_title == '1000'):
             #         title = "Full stack web developer"
             #     else:
             #         if (y.job_title == '2000'):
             #             title = "Mobile Application Developer"
             #         else:
             #             if (y.job_title == '3000'):
             #                 title = "Front end developer"
             #             else:
             #                 if (y.job_title == '4000'):
             #                     title = "Backend Developer"
             #     description=y.job_description
             #     print(title)
             #     print(description)
             # param={"title":title,
             #        "description":description}


             param={'param':obj}

             return render(request, 'new-post.html',param)
            except:

             return render(request,'new-post.html')
        else:
            datagetofemployee=intoresume.objects.filter(user_id=user.id)
            if(datagetofemployee.count()==0):
                return render(request, 'job-post.html')
            else:
                print("CCCCCCCCCCCCC");
                datagetofemployee = intoresume.objects.filter(user_id=user.id)
                #print(datagetofemployee)
                for y in datagetofemployee:
                    #for y in datagetofemployee:
                        gender = ""
                        title = ""
                        career_level = ""
                        degree_level = ""
                        sub_degree_level = ""
                        experience = ""
                        name=y.d_resume_name
                        email=y.d_resume_email
                        cnic=y.d_resume_cnic
                        mobile_number=y.d_resume_contact
                        dob=y.d_resume_dob
                        description=y.d_resume_description
                        skills= y.d_resume_skills
                        m = skills.split(',')
                        jskills = tuple(m)
                        status=y.d_resume_status
                        print(jskills[0])
                        if(y.d_resume_profile==''):
                         image=(os.path.join(settings.MEDIA_ROOT, '16201519-106.jpg'))
                        else:
                         image=y.d_resume_profile
                        print(image)
                        if (y.d_resume_title == '1000'):
                            title = "Full stack web developer"
                        else:
                            if (y.d_resume_title == '2000'):
                                title = "Mobile Application Developer"
                            else:
                                if (y.d_resume_title == '3000'):
                                    title = "Front end developer"
                                else:
                                    if (y.d_resume_title == '4000'):
                                        title = "Backend Developer"

                        if (y.d_resume_gender == '443'):
                            gender = "Male"
                        else:
                            if (y.d_resume_gender == '445'):
                                gender = "Female"
                            else:
                                if (y.d_resume_gender == '446'):
                                    gender = "Transparent"

                        if (y.d_resume_career_level == '686'):
                            career_level = "Intern/Student"
                        else:
                            if (y.d_resume_career_level == '868'):
                                career_level = "Entry Level"
                            else:
                                if (y.d_resume_career_level == '693'):
                                    career_level = "Experienced Professional"
                                else:
                                    if (y.d_resume_career_level == '698'):
                                        career_level = "Department Head"
                                    else:
                                        if (y.d_resume_career_level == '697'):
                                            career_level = "GM / CEO / Country Head / President"
                        if (y.d_resume_degreelevel == '900'):
                            degree_level = "Pharm-D"
                        else:
                            if (y.d_resume_degreelevel == '836'):
                                degree_level = "Non-Matriculation"
                            else:
                                if (y.d_resume_degreelevel == '838'):
                                    degree_level = "Matriculation/O-Level"
                                else:
                                    if (y.d_resume_degreelevel == '840'):
                                        degree_level = "Intermediate/A-Level"
                                    else:
                                        if (y.d_resume_degreelevel == '369'):
                                            degree_level = "Bachelor"
                                        else:
                                            if (y.d_resume_degreelevel == '373'):
                                                degree_level = "Master"
                                            else:
                                                if (y.d_resume_degreelevel == '844'):
                                                    degree_level = "MBBS/D-Pharm/BDS"
                                                else:
                                                    if (y.d_resume_degreelevel == '842'):
                                                        degree_level = "M-Phill"
                                                    else:
                                                        if (y.d_resume_degreelevel == '375'):
                                                            degree_level = "PHD/Doctorate"
                                                        else:
                                                            if (y.d_resume_degreelevel == '846'):
                                                                degree_level = "Certification"
                                                            else:
                                                                if (y.d_resume_degreelevel == '371'):
                                                                    degree_level = "Diploma"
                                                                else:
                                                                    if (y.d_resume_degreelevel == '1243'):
                                                                        degree_level = "Short Course"
                        if (y.d_resume_subdegreelevel == '2000'):
                            sub_degree_level = "CS"
                        else:
                            if (y.d_resume_subdegreelevel == '1500'):
                                sub_degree_level = "IT"
                            else:
                                if (y.d_resume_subdegreelevel == '1000'):
                                    sub_degree_level = "SE"
                        if (y.d_resume_experience == '0.5'):
                            experience = "Less Than 1 Year"
                        else:
                            if (y.d_resume_experience == '36'):
                                experience = "More Than 35 Years"
                            else:
                                experience = y.d_resume_experience

                        params={
                            "name" : name,
                            "email" : email,
                            "cnic" : cnic,
                            "gender" : gender,
                            "dob" : dob,
                            "mobile_number" : mobile_number,
                            "title" : title,
                            "experience" : experience,
                            "career_level" : career_level,
                            "degree_level" : degree_level,
                            "description" : description,
                            "skills" : jskills,
                            "image" : image,
                            "status":status,
                            "user_id" : user.id

                        }
                        #print(image)
                print("hahahah3")
                return render(request, 'job-post.html',params)
    else:
        print("hahahah4")
        return render(request,'confirmation.html')
    print("hahahah5")
    return render(request, 'new-post.html')

def randompassword():
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    size = random.randint(8, 12)
    return ''.join(random.choice(chars) for x in range(size))


# Create your views here.
def base(request):
    return render(request, 'base.html')


def tryy(request):
    return render(request, 'try.html')


def contact(request):
    return render(request, 'contact.html')


def newpost(request):
    return render(request, 'new-post.html')


def wantajob(request):
    return render(request, 'job-post.html')


def login(request):
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        rad = request.POST.get('rad')
        print(rad)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            print(username, email, password)
            user = User.objects.create(username=username, email=email)
            user.set_password(password)
            user.save()
            # username1=str(username)
            messages.success(request, f'Account created for {username}')
            #  form.save()
            # userget=User.objects.get()
            obj = get_random_string(length=6, allowed_chars='1234567890')
            mymodel = Type.objects.create(user_id=user.id, type=rad,emcon=str(obj),con=False)
            mymodel.save()
            send_mail(
                'Your Account Confirmation Code ',  # subject portion
                'Your Account Confirmation Code is ' + str(obj),  # message portion
                'skills.based.recommender@gmail.com',  # email from
                [user.email],  # email to
                fail_silently=False, )

            return redirect('/accounts/login/')
    else:
        form = UserRegisterForm()

    return render(request, 'signup.html', {'form': form})
@login_required
def confirmm(request):
     obj=get_random_string(length=6, allowed_chars='1234567890')
     user=request.user
     obj1=Type.objects.filter(user_id=user.id)
     obj1.update(emcon=str(obj))
     #print(user.email)
     send_mail(
        'Your Account Confirmation Code ',  # subject portion
        'Your Account Confirmation Code is ' + str(obj),  # message portion
        'skills.based.recommender@gmail.com',  # email from
        [user.email],  # email to
        fail_silently=False, )
     return render(request, 'confirmation.html')


def register(request):
    user=request.user
    obj=Type.objects.get(user_id=user.id)
    confirmcode = request.POST.get('con')
    if (str(obj.emcon) == confirmcode):
        #user = User(uname=object.uname, em=object.em, pas=object.pas, rad=object.rad)
        #user.save()
        obj1=Type.objects.filter(user_id=user.id)
        obj1.update(con="True")
        response = redirect('/goprofile/')
        return response
    else:
        param = {'error': "Enter Correct Code"}
        return render(request, 'confirmation.html', param)





@login_required
def profile(request):
    return render(request, 'profile.html')


def forget(request):
    return render(request, 'forget.html')


def sendmail(request):
    em = request.POST.get('em')
    try:

        instance = User.objects.get(em=em)
        newpas = randompassword()
        print(newpas)
        User.objects.filter(em=em).update(pas=newpas)
        send_mail(
            'Your Account Reset password ',  # subject portion
            'Your Account Reset password is ' + newpas,  # message portion
            'skills.based.recommender@gmail.com',  # email from
            [em],  # email to
            fail_silently=False, )
        param = {'error': 'Mail successfully sent..!'}
        return render(request, 'login.html', param)
    except:
        param = {'error': 'No Record Found...! Please Enter Correct Email..!'}
        return render(request, 'forget.html', param)

@login_required
def uploadresume(request):
    return render(request, 'upload-resume.html')

@login_required
def jobdatainsertion(request):
    user=request.user
    job_title=request.POST.get('job_title')
    job_description=request.POST.get('job_description')
    job_skills=request.POST.get('job_skills')
    job_skills_periority=request.POST.get('job_skills_periority')
    job_career_level=request.POST.get('job_career_level')
    job_career_level_periority=request.POST.get('job_career_level_periority')
    job_positions=request.POST.get('job_positions')
    job_country=request.POST.get('job_country')
    job_degree_level=request.POST.get('job_degree_level')
    job_degree_level_periority=request.POST.get('job_degree_level_periority')
    job_min_experience=request.POST.get('job_min_experience')
    job_experience_periority=request.POST.get('job_experience_periority')
    job_min_sallery=request.POST.get('job_min_sallery')
    job_max_sallery=request.POST.get('job_max_sallery')
    job_prefrence=request.POST.get('job_prefrence')
    job_prefrence_periority=request.POST.get('job_prefrence_periority')
    #print(job_title,job_description,job_skills,job_skills_periority,job_career_level,job_career_level_periority,job_positions,job_country,job_degree_level,job_degree_level_periority,job_min_experience,job_experience_periority,job_min_sallery,job_max_sallery,job_prefrence,job_prefrence_periority)
    try:
     obj=Job.objects.create(user_id=user.id,job_title=job_title,job_description=job_description,job_skills=job_skills,job_skills_periority=job_skills_periority,job_career_level=job_career_level,job_career_level_periority=job_career_level_periority,job_positions=job_positions,job_country=job_country,job_degree_level=job_degree_level,job_degree_level_periority=job_degree_level_periority,job_min_experience=job_min_experience,job_experience_periority=job_experience_periority,job_min_sallery=job_min_sallery,job_max_sallery=job_max_sallery,job_prefrence=job_prefrence,job_prefrence_periority=job_prefrence_periority)
     obj.save()
     obj1=Job.objects.filter(user_id=user.id,job_title=job_title,job_description=job_description,job_skills=job_skills,job_skills_periority=job_skills_periority,job_career_level=job_career_level,job_career_level_periority=job_career_level_periority,job_positions=job_positions,job_country=job_country,job_degree_level=job_degree_level,job_degree_level_periority=job_degree_level_periority,job_min_experience=job_min_experience,job_experience_periority=job_experience_periority,job_min_sallery=job_min_sallery,job_max_sallery=job_max_sallery,job_prefrence=job_prefrence,job_prefrence_periority=job_prefrence_periority)
     obj1.update(slug=obj.id)
     messages.success(request, 'Job Created Successfully')
     return redirect('/goprofile/')
    except:
      print("error")

    '''form = job_data_insertion(request.POST or None)
     if (form.is_valid()):
         form.save()
      print("haha")
     else:
       print("error")'''
    return render(request, 'job_data_insertion_successful.html')

@login_required
def upload(request):
    uploaded_file = request.FILES['document']
    fs = FileSystemStorage()
    fs.save(uploaded_file.name, uploaded_file)
    upload_file = uploaded_file.name
    from pyresparser import ResumeParser
    data = ResumeParser(os.path.join(settings.MEDIA_ROOT, uploaded_file.name)).get_extracted_data()
    print(data)
    str = data['skills']
    from nltk.stem import WordNetLemmatizer
    lemmatizer = WordNetLemmatizer()
    lemmatized_output = ' '.join([lemmatizer.lemmatize(w) for w in str])
    print(lemmatized_output)
    word_list = nltk.word_tokenize(lemmatized_output)
    print(word_list)
    ret = ''' [']'''
    text = ""
    for char in word_list:
        if char not in ret:
            text = text + char + ","
    print(text)
    # str1 = str.replace(']','').replace('[','')
    # l = str1.replace('"','').split(",")
    # print(l)

    # l = [ele.strip().split(';') for ele in str]
    # print(l)

    params = {
        "name": data['name'],
        "email": data['email'],
        "mobile_number": data['mobile_number'],
        "degree": data['degree'],
        "designation": data["designation"],
        # "skills" : data['skills'],
        "skills": text,
        "total_experience": data['total_experience'],
        # "update" : l
    }
    '''
    upload_file = ''
    if request.method == 'POST':
        # uploaded_file = ''
        # os.remove(os.path.join(settings.MEDIA_ROOT, uploaded_file.name))
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        upload_file = uploaded_file.name
        print(uploaded_file.name)
        # print(uploaded_file.size)
        if (upload_file != ''):
            pdfFileObj = open(upload_file, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
            # number of pages in pdf
            print(pdfReader.numPages)
            # a page object
            pageObj = pdfReader.getPage(0)
            te = ""
            # x = re.findall("Phone:", pageObj.extractText())
            print(pageObj.extractText())
            # match = re.search(r'(?:[a-z0-9!#$%&*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])+', pageObj.extractText())
            match = re.search(r'[\w\.-]+@[\w\.-]+', pageObj.extractText())
            match1 = re.search(
                r'(?:(?:\+?([1-9]|[0-9][0-9]|[0-9][0-9][0-9])\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([0-9][1-9]|[0-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?',
                pageObj.extractText())
            regex = re.search(r'[^()0-9-]+', pageObj.extractText())
            if (match):
                print(match)
            else:
                print('No match')
            if (match1):
                print(match1)
            else:
                print('No Number match')
            if (regex):
                print(regex)
            else:
                print('No match')
        # os.remove(os.path.join(settings.MEDIA_ROOT, upload_file))
        else:
            print('upload file')
        pdfFileObj.close()
        os.remove(os.path.join(settings.MEDIA_ROOT, uploaded_file.name))
        '''
    os.remove(os.path.join(settings.MEDIA_ROOT, uploaded_file.name))
    return render(request, 'confirm.html',params)

@login_required
def ret(request):
    return render(request, 'upload-resume.html')

@login_required
def feedback(request):
    user=request.user
    if(request.user.is_superuser):
        if request.method == 'POST':
            sub = request.POST.get('sub')
            disc = request.POST.get('ta')
            user = request.user
            print(sub, disc)
            if (sub == "" and disc == ""):
                messages.success(request, f'Kindly fill all the fields..!')
                return redirect('/feedback/')
            else:
                obj1 = FeedBack.objects.filter(slug=sub)
                obj1.update(response=disc)

                messages.success(request, f'Thanks for your Feedback {user.username}')
                return redirect('/feedback/')
        try:
            obj = FeedBack.objects.all()
            param = {'param': obj}
            return render(request, 'adminfeedback.html', param)
        except:
            return render(request, 'adminfeedback.html')

        return render(request, 'feedback.html')
    else:
        if request.method == 'POST':
            sub=request.POST.get('sub')
            disc=request.POST.get('ta')
            user=request.user
            print(sub,disc)
            if (sub!="" and disc!=""):
                obj = FeedBack.objects.create(user_id=user.id, subject=sub,disc=disc)
                obj.save()
                obj1=FeedBack.objects.filter(user_id=user.id,subject=sub,disc=disc)
                obj1.update(slug=obj.id)
                # username1=str(username)
                messages.success(request, f'Thanks for your Feedback {user.username}')
                return redirect('/feedback/')
        try:
            obj =FeedBack.objects.filter(user_id=user.id)
            param={'param':obj}
            return render(request,'feedback.html',param)
        except:
            return render(request,'feedback.html')

        return render(request, 'feedback.html')

@login_required
def adminfeedback(request):
    return render(request, 'adminfeedback.html')

@login_required
def delfeedback(request,slug):
    if (slug!=""):

        obj=FeedBack.objects.filter(slug=slug)
        obj.delete()
        return redirect('/feedback/')
    return render(request,'adminfeedback.html')


def analyse(request):
    sub=""
    disc=""
    text=""
    polarity = 0
    positive = 0
    wpositive = 0
    spositive = 0
    negative = 0
    wnegative = 0
    snegative = 0
    neutral = 0
    try:
        obj=FeedBack.objects.all()
        for data in obj:
                text=TextBlob(data.subject+" "+data.disc)
                print(text)
                polarity+=text.sentiment.polarity
                if (text.sentiment.polarity == 0):  # adding reaction of how people are reacting to find average later
                    neutral += 1
                elif (text.sentiment.polarity > 0 and text.sentiment.polarity <= 0.3):
                    wpositive += 1
                elif (text.sentiment.polarity > 0.3 and text.sentiment.polarity <= 0.6):
                    positive += 1
                elif (text.sentiment.polarity > 0.6 and text.sentiment.polarity <= 1):
                    spositive += 1
                elif (text.sentiment.polarity > -0.3 and text.sentiment.polarity <= 0):
                    wnegative += 1
                elif (text.sentiment.polarity > -0.6 and text.sentiment.polarity <= -0.3):
                    negative += 1
                elif (text.sentiment.polarity > -1 and text.sentiment.polarity <= -0.6):
                    snegative += 1
        #print('polarity',polarity,'positive',positive,'wpositive',wpositive,'spositive',spositive,'wnegative',wnegative,'negative',negative,'snegative',snegative)
        param={
        'pol':str(polarity),
        'net':neutral,
        'wpos':wpositive,
        'pos':positive,
        'spos':spositive,
        'neg':negative,
        'sneg':snegative,
        'wneg': wnegative,}
        print(wnegative,polarity)
        return render(request, 'sentiment.html',param)
    except:
        print("hahaha")
    return render(request,'sentiment.html')





@login_required
def insertintoresume(request):
    return render(request, 'insert_into_resume.html')

@login_required
def resumedataintodatabse(request):
    user=request.user
    d_resume_title=request.POST.get('d_resume_title')
    d_resume_name=request.POST.get('d_resume_name')
    d_resume_email=request.POST.get('d_resume_email')
    d_resume_dob=request.POST.get('d_resume_dob')
    d_resume_cnic=request.POST.get('d_resume_cnic')
    d_resume_contact=request.POST.get('d_resume_contact')
    d_resume_gender=request.POST.get('d_resume_gender')
    d_resume_region=request.POST.get('d_resume_region')
    d_resume_career_level=request.POST.get('d_resume_career_level')
    d_resume_degreelevel=request.POST.get('d_resume_degreelevel')
    d_resume_subdegreelevel=request.POST.get('d_resume_subdegreelevel')
    d_resume_skills=request.POST.get('d_resume_skills')
    d_resume_experience=request.POST.get('d_resume_experience')
    d_resume_description=request.POST.get('d_resume_description')
    checking=intoresume.objects.filter(d_resume_cnic=d_resume_cnic)
    print(checking)
    if intoresume.objects.filter(user_id=user.id):
        print("User Already exists")
        return render(request, 'userdataalreadyexist.html')

    else:
        obj = intoresume.objects.create(user_id=user.id, d_resume_title=d_resume_title, d_resume_name=d_resume_name,
                                        d_resume_email=d_resume_email,d_resume_dob=d_resume_dob, d_resume_cnic=d_resume_cnic,
                                        d_resume_contact=d_resume_contact, d_resume_gender=d_resume_gender,
                                        d_resume_region=d_resume_region, d_resume_career_level=d_resume_career_level,
                                        d_resume_degreelevel=d_resume_degreelevel,
                                        d_resume_subdegreelevel=d_resume_subdegreelevel,
                                        d_resume_skills=d_resume_skills, d_resume_experience=d_resume_experience,d_resume_description=d_resume_description)
        obj.save()
        obj1 = intoresume.objects.filter(user_id=user.id, d_resume_title=d_resume_title, d_resume_name=d_resume_name,
                                         d_resume_email=d_resume_email, d_resume_dob=d_resume_dob,d_resume_cnic=d_resume_cnic,
                                         d_resume_contact=d_resume_contact, d_resume_gender=d_resume_gender,
                                         d_resume_region=d_resume_region, d_resume_career_level=d_resume_career_level,
                                         d_resume_degreelevel=d_resume_degreelevel,
                                         d_resume_subdegreelevel=d_resume_subdegreelevel,
                                         d_resume_skills=d_resume_skills, d_resume_experience=d_resume_experience,d_resume_description=d_resume_description)
        obj1.update(slug=obj.id)
    return render(request, 'resume_data_into_databse.html')


@login_required
def deljob(request,slug):
    user=request.user
    if(request.user.is_superuser):
        obj=Job.objects.filter(slug=slug)
        for y in obj:
            y.recommend_request=False
            y.request_status="Request Rejected"
            y.save()
        return redirect('/jobrequests/')
    else:
        obj = Job.objects.filter(user_id=user.id, slug=slug)
        obj.delete()
    return redirect('/goprofile/')

@login_required
def viewjob(request,slug):
    user = request.user
    obj = Job.objects.filter( slug=slug)     #issue ...i want to get the id or job....not user
    param = {'param': obj}
    if (request.user.is_superuser):
        return render(request, 'adminviewjob.html', param)
    else:
        obj = Job.objects.filter(user_id=user.id, slug=slug)
        return render(request,'viewjob.html',param)




@login_required
def jobdataget(request,slug): #Main function
 user=request.user
 print(slug)
 count = 0

 alldata = Job.objects.get(user_id=user.id,slug=slug)
 x = alldata.job_skills
 z = x.split(',')  # gte skills from databse and convert them into arrays
 skills = tuple(z)
 lengthofskills = len(skills)

 try:
    recommended.objects.filter(user_id=user.id,forjob=slug).delete()
    print("waleeeeeeeeeeeeeeeeeeeeeeeeed")
    employeedata = intoresume.objects.filter(d_resume_title=alldata.job_title,d_resume_status=True)

    for x in employeedata:

        l = x.d_resume_skills
        m = l.split(',')
        jskills = tuple(m)

        for skill in skills:  # skills comparisons
            for jskill in jskills:
                if (skill == jskill):
                    count = count + alldata.job_experience_periority

        #print(count)
        #print("out of loop")

        y = x.d_resume_career_level
        s = x.d_resume_degreelevel
        g = x.d_resume_gender
        e = x.d_resume_experience
        z = x.d_resume_cnic
        if (alldata.job_career_level <= y):  # 693<=693    count==3
            count = count + alldata.job_career_level_periority
         #   print(count)
            intoresume.objects.filter(d_resume_cnic=z).update(d_resume_counter=count)
          #  print("out 1st counter")
        if (alldata.job_degree_level <= s):  # 373<=1570         count=3+5==8
            count = count + alldata.job_degree_level_periority
           # print(count)
            intoresume.objects.filter(d_resume_cnic=z).update(d_resume_counter=count)
            #print("out 2nd counter")
        if (alldata.job_prefrence == g):  # 445<=445   count=3+3   6
            count = count + alldata.job_prefrence_periority
            #print(count)
            intoresume.objects.filter(d_resume_cnic=z).update(d_resume_counter=count)
        if (alldata.job_min_experience <= e):  # 445<=445   count=3+3   6
            count = count + alldata.job_experience_periority
            #print(count)
            intoresume.objects.filter(d_resume_cnic=z).update(d_resume_counter=count)
            #print("out 4th counter")
        count = 0
        #print(count)
    # print(alldata.job_skills)
    #print("I am out of loop")

    #print("Noe Checking the Highest counter value")
    counters = intoresume.objects.filter(
        d_resume_title=alldata.job_title)  # geting  value of counter from counter field .. jo relevent counters hain unki vlaues array ma same krna laga hain
    arr = []

    for coun in counters:
        arr.append(coun.d_resume_counter)
    #print(arr)
    hcounter = max(arr)  # max value get ki waca hi
    arr.sort(reverse=True)
    #print(arr)
    #print(hcounter)
    arr2 = []
    noofposition = alldata.job_positions  # required counters for company
    #print(noofposition)
    lengthofarray = len(arr)  # calculate the total counters in array
    #print(arr)

    if (noofposition <= lengthofarray):  # if require employeers are less then availables then
        for i in range(0,
                       noofposition):  # loop that will return us the counters and store into array acoording to company requrements
            arr2.append(arr[i])
    else:  # nahi to jitna available hain array ma wo hi copy kr do
        for i in range(0, len(arr)):
            arr2.append(arr[i])
    #print(arr2)

    length = len(arr2)
    #print("length", length)
    final = list()
    recommended.objects.filter(user_id=user.id, forjob=slug).delete()
    for x in range(length):  # ab bari bar sb counter ki value database ca nikalni ha
        datagetofemployee = intoresume.objects.filter(d_resume_counter=arr2[x],d_resume_title=alldata.job_title)
        #print("counter", arr2[x])

        # statuses.append(datagetofemployee)   #jitna b ay un ko in array ma store krwa dia  statuses. ab is ko ma pamas ma pass kr do ga
        mycounter=0;
        for y in datagetofemployee:
         if(mycounter<noofposition):
            print("hehe");
            gender = ""
            title = ""
            career_level = ""
            degree_level = ""
            sub_degree_level = ""
            experience = ""
            if (y.d_resume_title == '1000'):
                title = "Full stack web developer"
            else:
                if (y.d_resume_title == '2000'):
                    title = "Mobile Application Developer"
                else:
                    if (y.d_resume_title == '3000'):
                        title = "Front end developer"
                    else:
                        if (y.d_resume_title == '4000'):
                            title = "Backend Developer"

            if (y.d_resume_gender == '443'):
                gender = "Male"
            else:
                if (y.d_resume_gender == '445'):
                    gender = "Female"
                else:
                    if (y.d_resume_gender == '446'):
                        gender = "Transparent"

            if (y.d_resume_career_level == '686'):
                career_level = "Intern/Student"
            else:
                if (y.d_resume_career_level == '868'):
                    career_level = "Entry Level"
                else:
                    if (y.d_resume_career_level == '693'):
                        career_level = "Experienced Professional"
                    else:
                        if (y.d_resume_career_level == '698'):
                            career_level = "Department Head"
                        else:
                            if (y.d_resume_career_level == '697'):
                                career_level = "GM / CEO / Country Head / President"
            if (y.d_resume_degreelevel == '900'):
                degree_level = "Pharm-D"
            else:
                if (y.d_resume_degreelevel == '836'):
                    degree_level = "Non-Matriculation"
                else:
                    if (y.d_resume_degreelevel == '838'):
                        degree_level = "Matriculation/O-Level"
                    else:
                        if (y.d_resume_degreelevel == '840'):
                            degree_level = "Intermediate/A-Level"
                        else:
                            if (y.d_resume_degreelevel == '369'):
                                degree_level = "Bachelor"
                            else:
                                if (y.d_resume_degreelevel == '373'):
                                    degree_level = "Master"
                                else:
                                    if (y.d_resume_degreelevel == '844'):
                                        degree_level = "MBBS/D-Pharm/BDS"
                                    else:
                                        if (y.d_resume_degreelevel == '842'):
                                            degree_level = "M-Phill"
                                        else:
                                            if (y.d_resume_degreelevel == '375'):
                                                degree_level = "PHD/Doctorate"
                                            else:
                                                if (y.d_resume_degreelevel == '846'):
                                                    degree_level = "Certification"
                                                else:
                                                    if (y.d_resume_degreelevel == '371'):
                                                        degree_level = "Diploma"
                                                    else:
                                                        if (y.d_resume_degreelevel == '1243'):
                                                            degree_level = "Short Course"
            if (y.d_resume_subdegreelevel == '2000'):
                sub_degree_level = "CS"
            else:
                if (y.d_resume_subdegreelevel == '1500'):
                    sub_degree_level = "IT"
                else:
                    if (y.d_resume_subdegreelevel == '1000'):
                        sub_degree_level = "SE"
            if (y.d_resume_experience == '0.5'):
                experience = "Less Than 1 Year"
            else:
                if (y.d_resume_experience == '36'):
                    experience = "More Than 35 Years"
                else:
                    experience = y.d_resume_experience
            objj = recommended.objects.create(user_id=user.id,
                                              d_resume_title=title, d_resume_name=y.d_resume_name,
                                              d_resume_email=y.d_resume_email, d_resume_cnic=y.d_resume_cnic,
                                              d_resume_gender=gender, d_resume_region=y.d_resume_region,
                                              d_resume_career_level=career_level, d_resume_degreelevel=degree_level,
                                              d_resume_subdegreelevel=sub_degree_level,
                                              d_resume_skills=y.d_resume_skills, d_resume_experience=experience,
                                              d_resume_counter=y.d_resume_counter,forjob=slug )
            objj.save()
            objj1=recommended.objects.filter( d_resume_title=title, d_resume_name=y.d_resume_name,
                                              d_resume_email=y.d_resume_email, d_resume_cnic=y.d_resume_cnic,
                                              d_resume_gender=gender, d_resume_region=y.d_resume_region,
                                              d_resume_career_level=career_level, d_resume_degreelevel=degree_level,
                                              d_resume_subdegreelevel=sub_degree_level,
                                              d_resume_skills=y.d_resume_skills, d_resume_experience=experience,
                                              d_resume_counter=y.d_resume_counter,forjob=slug)
            objj1.update(slug=objj.id)
            mycounter=mycounter+1;
    model = recommended.objects.filter(user_id=user.id,forjob=slug)
    param = {'final': model}
    return render(request, 'jobdataget.html', param)
 except:
     messages.error(request,'Sorry No Candidate found for your job..!')
     return redirect('/goprofile/')


@login_required
def recommendData(request):
     user=request.user
     model=recommended.objects.filter(user_id=user.id)
     param={'final':model}
     return render(request,'jobdataget.html',param)




@login_required
def viewdetailofcandidate(request):
    return render(request, 'view_detail_of_candidate.html')


class ArticleDetailView(DetailView):
    print("hahaha")
    model = recommended
    template_name = 'article_detail.html'

@login_required
def call_for_interviews(request,slug):
    user=request.user  # ya us user ki id get kr raha ha jisw anai tjobs create ki hain
    user_email=user.email  # uska email address b et kr raha ha

    '''for x in data:
        title = x.d_resume_title
        name = x.d_resume_name  # variable name copy paste ki waja ca aca hain.........
        email = x.d_resume_email  # Ab ab recommended k table ca data utha k new table ma dal raha hain interview wala
        cnic = x.d_resume_cnic
        gender = x.d_resume_gender
        region = x.d_resume_region
        careerlevel = x.d_resume_career_level
        degreelevel = x.d_resume_degreelevel
        subdegreelevel = x.d_resume_subdegreelevel
        skills = x.d_resume_skills
        experience = x.d_resume_experience
        counter = x.d_resume_counter

    objj = call_for_interview.objects.create(user_id=user.id,d_resume_title=title, d_resume_name=name,
                              d_resume_email=email, d_resume_cnic=cnic,
                              d_resume_gender=gender, d_resume_region=region,
                              d_resume_career_level=careerlevel, d_resume_degreelevel=degreelevel,
                              d_resume_subdegreelevel=subdegreelevel, d_resume_skills=skills,
                              d_resume_experience=experience, d_resume_counter=counter,
                              slug="1")
    objj.save()

    obj1 = call_for_interview.objects.filter(user_id=user.id,d_resume_title=title, d_resume_name=name,
                              d_resume_email=email, d_resume_cnic=cnic,
                              d_resume_gender=gender, d_resume_region=region,
                              d_resume_career_level=careerlevel, d_resume_degreelevel=degreelevel,
                              d_resume_subdegreelevel=subdegreelevel, d_resume_skills=skills,
                              d_resume_experience=experience, d_resume_counter=counter)
    obj1.update(slug=objj.id)
    x=objj.id
    for y in alldata:
        jobtitle=y.job_title      # is loop ma wo user ki job ka title wagara la raha ha .. But agar uski 2,3 jobs hain to issue aya ga is lia specific job ki id hi get ho ......
        jobdescription=y.job_description
    if (jobtitle == '1000'):
        title = "Full stack web developer"
    else:
        if (jobtitle == '2000'):
            title = "Mobile Application Developer"
        else:
            if (jobtitle == '3000'):
                title = "Front end developer"
            else:
                if (jobtitle == '4000'):
                    title = "Backend Developer"'''


    data1 = recommended.objects.filter(user_id=user.id, slug=slug)
    data1.update(calforinter=True)
    data=recommended.objects.get(user_id=user.id, slug=slug)
    forjob=data.forjob
    jobobject=Job.objects.get(user_id=user.id,slug=forjob)
    title=""
    jobdescription=jobobject.job_description
    minsalary=jobobject.job_min_sallery
    maxsalary=jobobject.job_max_sallery
    if (jobobject.job_title == '1000'):
        title = "Internship"
    else:
        if (jobobject.job_title == '2000'):
            title = "Part Time Job"
        else:
            if (jobobject.job_title == '3000'):
                title = "Regular Jobr"
            else:
                if (jobobject.job_title == '4000'):
                    title = "Regular plus Overtime"
    print(title)
    msg ="You have a call for Interview from an Organization "+"\n"+ "Job_Title : " + str(title) + "\n" + "Job_Description : " + str(
        jobdescription) + "\n" +"Minimum Salary : "+str(minsalary)+"\n"+"Max Salary : "+str(maxsalary)+"\n" "Please Contact at This Email Address : " + str(user_email)
    send_mail(
        'Interview of Job',  # subject portion
         msg,
        'skills.based.recommender@gmail.com',  # email from
        [data.d_resume_email ],  # email to
        fail_silently=False, )
    messages.success(request,"Successfully called for Interview")
    return redirect('/recommended/')



@login_required
def hired(request,slug):
    user=request.user  # ya us user ki id get kr raha ha jisw anai tjobs create ki hain
    user_email=user.email  # uska email address b et kr raha ha
    data1 = recommended.objects.filter(user_id=user.id, slug=slug)
    data1.update(hired=True)
    data=recommended.objects.get(user_id=user.id, slug=slug)
    forjob=data.forjob
    jobobject=Job.objects.get(user_id=user.id,slug=forjob)
    title=""
    jobdescription=jobobject.job_description
    minsalary=jobobject.job_min_sallery
    maxsalary=jobobject.job_max_sallery
    if (jobobject.job_title == '1000'):
        title = "Internship"
    else:
        if (jobobject.job_title == '2000'):
            title = "Part Time Job"
        else:
            if (jobobject.job_title == '3000'):
                title = "Regular Jobr"
            else:
                if (jobobject.job_title == '4000'):
                    title = "Regular plus Overtime"
    print(title)
    msg ="You are hired in an Organization "+"\n"+ "Job_Title : " + str(title) + "\n" + "Job_Description : " + str(
        jobdescription) + "\n" +"Minimum Salary : "+str(minsalary)+"\n"+"Max Salary : "+str(maxsalary)+"\n" "Please Contact at This Email Address : " + str(user_email)
    send_mail(
        'Hired',  # subject portion
         msg,
        'skills.based.recommender@gmail.com',  # email from
        [data.d_resume_email ],  # email to
        fail_silently=False, )
    messages.success(request,"Successfully called for Interview")
    return redirect('/hired/')


def gohire(request):
    user = request.user
    inter = recommended.objects.filter(user_id=user.id, calforinter=True,hired=True)
    print(inter)
    param = {
        "finaldatas": inter
    }
    return render(request, 'hired.html', param)


@login_required
def interviews(request):
    user=request.user
    inter=recommended.objects.filter(user_id=user.id,calforinter=True,hired=False)
    print(inter)
    param = {
        "finaldatas": inter
        }
    return render(request, 'interviews.html',param)


def upload_resume_data(request):
    # print(datetime.datetime.now())
    form = uploaded_resume_data_into_databse(request.POST or None)
    if (form.is_valid()):
        form.save()
        print("haha")
    else:
        print("error")
    return render(request, 'uploaded_resume_data_into_databse.html')

def delcallforinterview(request,slug):
    user=request.user
    obj=recommended.objects.filter(user_id=user.id,slug=slug)
    obj.update(calforinter=False)
    return redirect('/interviews/')


class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        #id=request.POST.get("user_id")   #yaha pa get krni ha wo id but error a jata ha yaha tk ni ati
        user=request.user
        #print(user.id)#karo test
        #obj=intoresume.objects.filter(user_id=user.id)
        datagetofemployee = intoresume.objects.filter(user_id=user.id)
        print(datagetofemployee)
        for y in datagetofemployee:
                gender = ""
                title = ""
                career_level = ""
                degree_level = ""
                sub_degree_level = ""
                experience = ""
                name = y.d_resume_name
                email = y.d_resume_email
                cnic = y.d_resume_cnic
                mobile_number = y.d_resume_contact
                dob = y.d_resume_dob
                description = y.d_resume_description
                skills = y.d_resume_skills
                image = y.d_resume_profile
                print(image)
                if (y.d_resume_title == '1000'):
                    title = "Full stack web developer"
                else:
                    if (y.d_resume_title == '2000'):
                        title = "Mobile Application Developer"
                    else:
                        if (y.d_resume_title == '3000'):
                            title = "Front end developer"
                        else:
                            if (y.d_resume_title == '4000'):
                                title = "Backend Developer"

                if (y.d_resume_gender == '443'):
                    gender = "Male"
                else:
                    if (y.d_resume_gender == '445'):
                        gender = "Female"
                    else:
                        if (y.d_resume_gender == '446'):
                            gender = "Transparent"

                if (y.d_resume_career_level == '686'):
                    career_level = "Intern/Student"
                else:
                    if (y.d_resume_career_level == '868'):
                        career_level = "Entry Level"
                    else:
                        if (y.d_resume_career_level == '693'):
                            career_level = "Experienced Professional"
                        else:
                            if (y.d_resume_career_level == '698'):
                                career_level = "Department Head"
                            else:
                                if (y.d_resume_career_level == '697'):
                                    career_level = "GM / CEO / Country Head / President"
                if (y.d_resume_degreelevel == '900'):
                    degree_level = "Pharm-D"
                else:
                    if (y.d_resume_degreelevel == '836'):
                        degree_level = "Non-Matriculation"
                    else:
                        if (y.d_resume_degreelevel == '838'):
                            degree_level = "Matriculation/O-Level"
                        else:
                            if (y.d_resume_degreelevel == '840'):
                                degree_level = "Intermediate/A-Level"
                            else:
                                if (y.d_resume_degreelevel == '369'):
                                    degree_level = "Bachelor"
                                else:
                                    if (y.d_resume_degreelevel == '373'):
                                        degree_level = "Master"
                                    else:
                                        if (y.d_resume_degreelevel == '844'):
                                            degree_level = "MBBS/D-Pharm/BDS"
                                        else:
                                            if (y.d_resume_degreelevel == '842'):
                                                degree_level = "M-Phill"
                                            else:
                                                if (y.d_resume_degreelevel == '375'):
                                                    degree_level = "PHD/Doctorate"
                                                else:
                                                    if (y.d_resume_degreelevel == '846'):
                                                        degree_level = "Certification"
                                                    else:
                                                        if (y.d_resume_degreelevel == '371'):
                                                            degree_level = "Diploma"
                                                        else:
                                                            if (y.d_resume_degreelevel == '1243'):
                                                                degree_level = "Short Course"
                if (y.d_resume_subdegreelevel == '2000'):
                    sub_degree_level = "CS"
                else:
                    if (y.d_resume_subdegreelevel == '1500'):
                        sub_degree_level = "IT"
                    else:
                        if (y.d_resume_subdegreelevel == '1000'):
                            sub_degree_level = "SE"
                if (y.d_resume_experience == '0.5'):
                    experience = "Less Than 1 Year"
                else:
                    if (y.d_resume_experience == '36'):
                        experience = "More Than 35 Years"
                    else:
                        experience = y.d_resume_experience

        params = {
                    "name": name,
                    "email": email,
                    "cnic": cnic,
                    "gender": gender,
                    "dob": dob,
                    "mobile_number": mobile_number,
                    "title": title,
                    "experience": experience,
                    "career_level": career_level,
                    "degree_level": degree_level,
                    "description": description,
                    "skills": skills,
                    "image": image,
                    "user_id": user.id

                }

        template = get_template('invoice.html')
        #context = {
         #   "invoice_id": 123,
          #  "customer_name": "John Cooper",
           # "amount": 1399.99,
            #"today": "Today",
        #}
        html = template.render(params)
        pdf = render_to_pdf('invoice.html', params)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename=%s" %(filename)  #'%s' revomed ''
            download = request.GET.get("download")
            if download:
                content = "attachment; filename=%s" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")

@login_required
def editprofile(request):
    user=request.user
    datagetofemployee = intoresume.objects.filter(user_id=user.id)
    for y in datagetofemployee:
        name = y.d_resume_name
        email = y.d_resume_email
        cnic = y.d_resume_cnic
        contact=y.d_resume_contact
        gender=y.d_resume_gender
        degree_level=y.d_resume_degreelevel
        sub_degree_level=y.d_resume_subdegreelevel
        title=y.d_resume_title
        career_level=y.d_resume_career_level
        experience=y.d_resume_experience
        mobile_number = y.d_resume_contact
        dob = y.d_resume_dob
        description = y.d_resume_description
        skills = y.d_resume_skills
        image = y.d_resume_profile
        region = y.d_resume_region
        print(image)

    params = {
        "name": name,
        "email": email,
        "cnic": cnic,
        "gender": gender,
        "dob": dob,
        "mobile_number": mobile_number,
        "title": title,
        "experience": experience,
        "career_level": career_level,
        "degree_level": degree_level,
        "description": description,
        "skills": skills,
        "image": image,
        "sub_degree_level": sub_degree_level,
        "contact": contact,
        "region": region
    }
    return render(request,"editprofile.html",params)
@login_required
def editprofile_into_database(request):
    user=request.user
    d_resume_title = request.POST.get('d_resume_title')
    d_resume_name = request.POST.get('d_resume_name')
    d_resume_email = request.POST.get('d_resume_email')
    d_resume_dob = request.POST.get('d_resume_dob')
    d_resume_cnic = request.POST.get('d_resume_cnic')
    d_resume_contact = request.POST.get('d_resume_contact')
    d_resume_gender = request.POST.get('d_resume_gender')
    d_resume_region = request.POST.get('d_resume_region')
    d_resume_career_level = request.POST.get('d_resume_career_level')
    d_resume_degreelevel = request.POST.get('d_resume_degreelevel')
    d_resume_subdegreelevel = request.POST.get('d_resume_subdegreelevel')
    d_resume_skills = request.POST.get('d_resume_skills')
    d_resume_experience = request.POST.get('d_resume_experience')
    d_resume_description = request.POST.get('d_resume_description')
    d_resume_profile = request.FILES.get('d_resume_profile1')
    print(d_resume_profile)
    x=intoresume.objects.filter(user_id=user)
    if(d_resume_profile==" "):
        print("NO image")
        for y in x:
            y.d_resume_title=d_resume_title
            y.d_resume_name=d_resume_name
            y.d_resume_email=d_resume_email
            y.d_resume_dob=d_resume_dob
            y.d_resume_cnic=d_resume_cnic
            y.d_resume_contact=d_resume_contact
            y.d_resume_gender=d_resume_gender
            y.d_resume_region=d_resume_region
            y.d_resume_career_level=d_resume_career_level
            y.d_resume_degreelevel=d_resume_degreelevel
            y.d_resume_subdegreelevel=d_resume_subdegreelevel
            y.d_resume_skills=d_resume_skills
            y.d_resume_experience=d_resume_experience
            y.d_resume_description=d_resume_description
            y.save()
    else:
            print("Yes image")
            for y in x:
                y.d_resume_title = d_resume_title
                y.d_resume_name = d_resume_name
                y.d_resume_email = d_resume_email
                y.d_resume_dob = d_resume_dob
                y.d_resume_cnic = d_resume_cnic
                y.d_resume_contact = d_resume_contact
                y.d_resume_gender = d_resume_gender
                y.d_resume_region = d_resume_region
                y.d_resume_career_level = d_resume_career_level
                y.d_resume_degreelevel = d_resume_degreelevel
                y.d_resume_subdegreelevel = d_resume_subdegreelevel
                y.d_resume_skills = d_resume_skills
                y.d_resume_experience = d_resume_experience
                y.d_resume_description = d_resume_description
                y.d_resume_profile=d_resume_profile
                y.save()


    return redirect('/goprofile/')


def contactdb(request):
    name=request.POST.get('names')
    email=request.POST.get('emails')
    subject=request.POST.get('subjects')
    message=request.POST.get('messages')
    print(name)
    obj=contactdbs.objects.create(name=name,email=email,subject=subject,message=message)
    obj.save()
    return render(request,"contact.html")

def changestatus(request):
    user=request.user
    x = intoresume.objects.filter(user_id=user)
    for y in x:
        if (y.d_resume_status == True):
            y.d_resume_status=False
        else:
            y.d_resume_status=True
    y.save()

    # obj = intoresume.objects.filter(user_id=user)
    # #print(status)
    # param = {
    #     "param" : obj
    # }
    return redirect('/goprofile/')


def recommendrequest(request):
    user=request.user
    obj=Job.objects.filter(user_id=user)
    for y in obj:
        if (y.recommend_request == False):
            y.recommend_request=True
            y.request_status = "Pending Request"
        else:
            if (y.recommend_request == True):
                y.request_status="Request Already Sent"
    y.save()
    return redirect('/goprofile/')
    # return render(request, 'recommend.html')

def jobrequests(request):      #request for recommend to admin
    obj=Job.objects.filter(recommend_request=True)
    param = {'param': obj}
    return render(request, 'jobrequests.html',param)


def acceptjob(request,slug):
    obj = Job.objects.filter(slug=slug)
    for y in obj:
        y.recommend_request = False
        y.request_status = "Request Accepted"
        y.save()
    return redirect('/jobrequests/')

#
# def messag(request):
#
#     #obj=messages.objcets.create(msgfrom=user.id , msg=mesg)
#     #obj.save()
#     seekerrecord=request.POST.get('seekerrecord')
#     print("hahhahh")
#     print(seekerrecord)
#     param={
#         "seekerrecord" : seekerrecord
#     }
#     return render(request,"messages.html", param)
#
# def mesage(request):
#     user = request.user
#     # datagetofemployee = messages.objects.filter(msgfrom=user.id)
#     mesg = request.POST.get('sub')
#     jobseeker = request.POST.get('record')
#     print(user.id)
#     print(mesg)
#     print(jobseeker)
#     return redirect("/messages/")

                  #Latest
