from django.conf.urls import url,include 
from django.contrib import admin
from forum.views import *
from django.contrib.auth import views 
from Feedback.views import *
from student.views import *
from contact.views import * 
from Article.views import *
from Login.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^test/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/',test),
]
contact = [url(r'^contact/$',contact),]

home = [url(r'^$',home_page.as_view(),name='home'),]

login =[#url(r'^accounts/login/$',Login.as_view()),
        url(r'^accounts/login/$',login_view),
        url(r'^accounts/logout/$',logout_view),]

register = [url(r'^accounts/register/$',signup),
			url(r'^accounts/register_success/$',register_success)]        

registration = [url(r'^registration$',registration),]
                #url(r'^(?P<faith_home>[-_\w]+)/$', registered_user.as_view(), name='first_name'),]
                #url(r'^registereduser/$',registered_user.as_view(),name = 'article')]

feedback = [url(r'^feedback/$',Give_Feedback),]
            #url(r'all/$',display_feedback.as_view(),name='display_feedback'),]

article = [url(r'^article/$',article),]
            #url(r'^article_dis/$',redirect.as_view(),name='article-detail')]

urlpatterns += home
urlpatterns += article        
urlpatterns += login  
urlpatterns += registration     
urlpatterns += contact
urlpatterns += feedback
urlpatterns += register
urlpatterns += staticfiles_urlpatterns()