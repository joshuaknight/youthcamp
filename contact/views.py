from django.shortcuts import render
from django.forms import formset_factory
from django.http import *
from django.template import *
from django.template.loader import *
from contact.forms import *
from contact.models import *
from django.core.mail import send_mail
from django.utils import timezone

def contact(request):
	form = formset_factory(Contact)
	formset = form()
	if request.method == 'POST':
		if not formset.is_valid():
			formset = form(request.POST)
		if formset.is_valid():
			for i in formset:
				i.save()
			message = """
				Thank You for Contacting username
				Please Wait Let Us Get Back to You
				"""
			return render(request,"base.html",{'message':message})
	return render(request,"contact.html",{'formset':formset,'now':timezone.now()})