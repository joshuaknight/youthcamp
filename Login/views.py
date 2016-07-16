from django.utils import timezone
from django.contrib.auth import authenticate,login,logout 
from django.shortcuts import *
from django.http import *
from .forms import *
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib import auth
from django.template.context_processors import csrf
from django.forms import formset_factory
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

def login_view(request):
	template_name = 'login.html'
	success_url = 'loggedin.html'
	unsuccess_url = 'invalid_login.html'
	post = request.POST
	form = AuthenticationForm
	if request.method == 'POST':
		username = post['username']
		password = post['password']
		user = authenticate(username=username,password=password)
		if user is not None:
			return render(request,success_url,{'full_name' : username})
		else:
			return render(request,unsuccess_url,{'full_name' : username})
	else:
		return render(request,template_name,{'formset':form})

def logout_view(request):
	logout(request)
	return render(request,'logout.html')

def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)	
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/accounts/register_success')
	args = {}
	args.update(csrf(request))			
	args['form'] = UserCreationForm()
	print args
	return render(request,'register.html',args)	

def register_success(request):
	return render(request,'register_success.html')	 			