from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.forms import formset_factory
from django.core.exceptions import ValidationError
from django.template.loaders import *
from django.template import *
from models import *
from django.http import *
from forum.forms import *		
from django.contrib.auth import authenticate,login
from student.models import *
from django.utils import timezone


class home_page(TemplateView):
	template_name = 'base.html'
	def get_context_data(self, **kwargs):
		context = super(home_page,self).get_context_data( **kwargs)
		context['now'] = timezone.now()
		return context
		
def test(request,year = 2016,month = 12):
	return HttpResponse('Hello Year : %r Hello Month : %r' %(year,month,))

def login_user(request):
	form = formset_factory(MyLogin)
	formset= form()
	if request.method == 'POST':	
		if formset.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username,password=password)	
			if user.is_active():
				login(request,user)
				message = "Successfully Logined In"
			else:
				return HttpResponseRedirect('')
		if not formset.is_valid():
			formset = form()
	else:
		formset=form()
	return render(request,'login.html',{'form':formset,'message':message})	

def signup_user(request):
	form = formset_factory(MySignup)
	formset = form()
	if request.method == "POST":
		#if not formset.is_valid():
		#	formset = form(request.POST)
		if formset.is_valid():
			for form in formset:
				form.save()
			return HttpResponseRedirect('/')
	return render(request,'signup.html',{'formset' : formset,})