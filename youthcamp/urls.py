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
contact = [url(r'^contact/$',contact,name='contact'),]

home = [url(r'^$',home_page.as_view(),name='home'),]

login =[#url(r'^accounts/login/$',Login.as_view()),
        url(r'^accounts/login/$',login_view,name='login'),
        url(r'^accounts/logout/$',logout_view),]

register = [url(r'^accounts/register/$',signup,name='signup'),
			url(r'^accounts/register_success/$',register_success)]        

registration = [url(r'^registration$',registration,name='register'),
                #url(r'^(?P<faith_home>[-_\w]+)/$', registered_user.as_view(), name='first_name'),]
                url(r'^registereduser/$',registered_user.as_view(),name = 'registered')]

comment = [url(r'^comment/$',Give_Feedback,name='comment'),
            url(r'comment/all/$',display_feedback.as_view(),name='display_comment'),]

article = [url(r'^article/$',article,name='article'),
            url(r'^article_dis/$',display_article.as_view(),name='article-detail')]

urlpatterns += home
urlpatterns += article        
urlpatterns += login  
urlpatterns += registration     
urlpatterns += contact
urlpatterns += comment
urlpatterns += register
urlpatterns += staticfiles_urlpatterns()