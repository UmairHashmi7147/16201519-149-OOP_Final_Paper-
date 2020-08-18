from django.urls import path,include
from . import views
from .views import ArticleDetailView, GeneratePDF

urlpatterns = [
    path('',views.gohome, name='base.html'),
    path('insertdata/',views.insertdata, name='insertdata.html'),
    path('viewdata/',views.viewdata, name='viewdata.html'),
    path('delpatient/<slug>/',views.delpatient,name="delpatient"),
    path('refer/<slug>/',views.refer,name="refer"),
    path('refered/',views.refered,name="refered"),
    path('updatedata/',views.updatedata,name="update"),
   
]
