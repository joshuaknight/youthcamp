from django.contrib.auth import authenticate,login 
from django.shortcuts import *
from django.http import *
from django.contrib import auth
from .forms import *
from django.core.context_processors import csrf
from django.forms import formset_factory

def login(request):
	c = formset_factory(Mylogin)
	f = c()
	return render('request','login.html',f)

def auth(request):
	username = request.POST.get('username','')
	password = request.POST.get('password','')
	user = authenticate(username = username,password=password)	
	
	if user is not None:
		login(request,user)
		return HttpResponseRedirect('/accounts/loggedin')	
	else:
		return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
	return render(request,'loggedin.html',{'full_name':request.user.username})	

def invalid_login(request):
	return render(request,'invalid_login.html')
def logout(request):
	logout(request)
	return render(request,'logout.html')	