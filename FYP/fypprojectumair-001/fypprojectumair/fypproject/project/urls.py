from django.urls import path,include
from . import views
from .views import ArticleDetailView, GeneratePDF

urlpatterns = [
    path('',views.base, name='base.html'),
    path('contact/',views.contact, name='contact.html'),
    path('newpost/',views.newpost, name='new-post.html'),
    path('wantajob/',views.wantajob, name='job-post.html'),
    path('login/',views.login, name='login.html'),
    path('signup/',views.signup, name='signup.html'),
    path('register/',views.register, name='signup.html'),
    path('profile/',views.profile, name='profile.html'),
    path('forget/', views.forget, name='forget'),
    path('sendmail/', views.sendmail, name='sendmail'),
    path('confirmm/', views.confirmm, name='confirmm'),
    path('upload-resume/', views.uploadresume, name='upload-resume'),
    path('job_data_insertion/', views.jobdatainsertion, name='job_data_insertion'),   #insert into database
    path('uploaded-resume/', views.upload, name='upload'),
    path('ret/', views.ret, name='ret'),
    path('feedback/', views.feedback, name='feedback'),
    path('insert_into_resume/', views.insertintoresume, name='insertintoresume'),   #insert direct data
    path('resume_data_into_databse/', views.resumedataintodatabse, name='resumedataintodatabse'),   #insert direct data into database
    path('job_data_get/<slug>', views.jobdataget, name='job_data_get'),   #after clicking on recommend button
    path('view_detail_of_candidate/', views.viewdetailofcandidate, name='viewdetailofcandidate'),
    path('<slug:slug>', ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('call_for_interview/<slug>', views.call_for_interviews, name='call_for_interview'),
    path('hired/<slug>', views.hired, name='hired'),
    path('hired/', views.gohire, name='hired1'),
    path('interviews/', views.interviews, name='interviews'),
    path('delfeedback/<slug>/',views.delfeedback,name="delfeedback"),
    path('goprofile/',views.goprofile,name="dds"),
    path('upload_resume_data/', views.upload_resume_data, name='upload_resume_data'),
    path('pdf/', GeneratePDF.as_view(), name='generate_pdf'),
    path('editprofile/',views.editprofile, name='editprofile'),
    path('editprofile_into_database/',views.editprofile_into_database, name='editprofile_into_database'),


    path('recommended/',views.recommendData,name="recommendData"),
    path('sentiment/',views.analyse,name="analyse"),
    path('deljob/<slug>/',views.deljob,name="deljob"),
    path('viewjob/<slug>/',views.viewjob,name="viewjob"),
    path('delcallforinterview/<slug>/',views.delcallforinterview,name="delcallforinterview"),

    path('contactdb/',views.contactdb,name="contactdb"),  #before 1 week evaluation
    # path('messages/',views.messag,name="messages"),  #before 1 week evaluation
    # path('mesage/',views.mesage,name="mesage")  #before 1 week evaluation
    path('changestatus/',views.changestatus,name="changestatus"), #before 1 week evaluation
    path('adminfeedback/',views.adminfeedback,name="adminfeedback"),  #before 1 week evaluation
    path('recommendrequest/', views.recommendrequest, name="recommendrequest"),
    path('jobrequests/', views.jobrequests, name="jobrequests"),
    path('acceptjob/<slug>', views.acceptjob, name="acceptjob")
]
