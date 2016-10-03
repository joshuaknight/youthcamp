from .views import *
from django.conf.urls import *

urlpatterns = [
		url(r'^register$',registration.as_view(),name = 'registration'),
		url(r'^registered/list$',registered_list.as_view(),name = 'registered_list'),
		url(r'^registered/(?P<faith_home>[\w-]+)/*$',student_location.as_view(),name = 'student_location'),
		url(r'^registered/list/male$',student_male.as_view(),name = 'student_male'),
		url(r'^registered/list/female$',student_female.as_view(),name = 'student_female'),
		url(r'^registered/(?P<pk>\d+)/detail$',student_detail.as_view(),name = 'student-detail'),
]