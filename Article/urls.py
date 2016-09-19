from .views import *
from django.conf.urls import *

urlpatterns = [
		url(r'^add$',article.as_view(),name = 'article'),
		url(r'^view$',display_article.as_view(),name = 'display_article'),		
]