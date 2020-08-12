from django.contrib import admin
from .models import FeedBack, Job, intoresume, recommended, Type, contactdbs
from django.contrib.auth.models import Group

# Register your models here.
class JobAdmin(admin.ModelAdmin):
    list_display = ('job_title','job_description','job_skills','job_career_level','job_degree_level','job_min_experience','job_min_sallery','job_max_sallery','job_prefrence')
    #list_filter = ('job_title',)


admin.site.register(Job,JobAdmin)
admin.site.register(Type)
admin.site.register(FeedBack)
admin.site.register(intoresume)
admin.site.register(recommended)
admin.site.register(contactdbs)




admin.site.unregister(Group)
admin.site.site_header="Skills Based Employee Recommender System Admin Pannel"

