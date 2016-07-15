from django.shortcuts import render
from django.forms import formset_factory
from django.http import *
from django.template import *
from django.template.loader import *
from contact.forms import *
from contact.models import *
from django.core.mail import send_mail
import datetime

def contact(request):
	form = formset_factory(Contact)
	formset = form()
	if request.method == 'POST':
		if not formset.is_valid():
			formset = form(request.POST)
		if formset.is_valid():
			for i in formset:
				i.save()
			return HttpResponseRedirect('/')
	return render(request,"contact.html",{'form':formset})