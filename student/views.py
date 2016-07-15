from django.contrib.auth.decorators import login_required,user_passes_test
from django.views.generic.base import TemplateView
from django.views.generic import ListView,DetailView
from django.http import *
from django.template.loader import *
from forum.models import *
from django.template import *
from django.shortcuts import *
from student.forms import *
from django.forms import formset_factory
from student.models import *
from django.utils import timezone
now = timezone.now()


def registration(request):
	form = formset_factory(RegisForm)
	formset = form()
	if request.method == "POST":
		if not formset.is_valid():
			formset = form(request.POST)
		if formset.is_valid():
			for form in formset:
				form.save()
			return HttpResponseRedirect('/')
	return render(request,'registration.html',{'form' : formset,'now':now})



class registered_user(DetailView):
	model = Registration
	template_name = 'registration_list.html'
	def get_context_data(self,**kwargs):
		context = super(registered_user,self).get_context_data(**kwargs)
		context['first_name'] = Registration.name_count.all()
		return context