from django.views.generic import ListView,DetailView
from django.core.mail import send_mail 
from django.http import *
from django.shortcuts import render,RequestContext
from Feedback.forms import *
from django.forms import formset_factory
from django.template.loader import *
from django.utils import timezone
from Feedback.models import *

now = timezone.now()
def Give_Feedback(request,name='all'):
    form = formset_factory(ContactForm)
    formset = form()
    if(request.method == 'POST'):
        formset = form(request.POST)
        if not formset.is_valid():
            formset = form(request.POST)
        if formset.is_valid():
            for i in formset:
                i.save()
        	return HttpResponseRedirect('/comment/all/')
    return render(request,'contact_form.html',{'formset':formset,'now':now})         

class display_feedback(ListView):
    template_name = 'thanks.html'
    model = Feedback

    def get_context_data(self,**kwargs):
        context = super(display_feedback,self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['date'] = Feedback.objects.all().values_list('Date')
        context['name'] = Feedback.count.all()
        context['name_list'] = Feedback.name_list.all()
        context['message_list'] = Feedback.message_list.all()
        return context   