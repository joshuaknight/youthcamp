from django.conf.urls.static import static
from django.conf.urls import url,include 
from django.contrib import admin
from .views import *
from django.conf import settings
from django.contrib.auth import views 
from contact.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from Article.models import *

admin.autodiscover()


urlpatterns = [
	url(r'^$',home_page.as_view(),name = 'home'),
    
    url(r'^admin/', admin.site.urls),    
    
    url(r'^contact$',contact.as_view(),name = 'contact'),		
  
    url(r'^student/',include('student.urls')),

    url(r'^article/',include('Article.urls')),
]