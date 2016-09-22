from .views import *
from django.conf.urls import *

urlpatterns = [
		url(r'^add$',article.as_view(),name = 'article'),
		url(r'^view$',display_article.as_view(),name = 'display_article'),		
		url(r'^detail/(?P<pk>\d+)/$',article_detail.as_view(),name = 'article_detail'),		
		url(r'^update/(?P<pk>\d+)/$',article_update.as_view(),name = 'article_update'),		
		url(r'^delete/(?P<pk>\d+)/$',article_delete.as_view(),name = 'article_delete'),		

]