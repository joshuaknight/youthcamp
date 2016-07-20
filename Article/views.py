from django.shortcuts import *
from django.http import *
from django.template.loader import *
from django.template import *
from django.core.exceptions import *
from django.forms import formset_factory
from django.forms import modelformset_factory
from Article.forms import *
from Article.models import *
from django.views.generic.base import RedirectView,TemplateView
import datetime
from django.contrib.auth.decorators import login_required

class redirect(TemplateView):
	template_name = 'disart.html'

	def get_context_data(self,**kwargs):
		context = super(redirect,self).get_context_data(**kwargs) 
		context['content'] = New_Article.author.all()
		return context


def article(request):
	form = formset_factory(MyArticle)
	formset = form()
	now = datetime.datetime.today()
	if request.method == "POST":
		if not formset.is_valid():
			formset = form(request.POST)
		if formset.has_changed():
			if formset.is_valid():
				for form in formset:
					form.save()
					return HttpResponseRedirect('/')
	return render(request,'article.html',{'formset' : formset,'now':now})

class display_article(TemplateView):
	template_name = "disart.html"	

	def get_context_data(self,**kwargs):
		context= super(display_article,self).get_context_data(**kwargs)
		context['author_count'] = New_Article.author_count.all()
		context['article_name'] = New_Article.article_list.all()
		return context

