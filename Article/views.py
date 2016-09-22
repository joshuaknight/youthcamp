from django.shortcuts import *
from django.http import *
from django.template.loader import *
from django.template import *
from django.core.exceptions import *
from django.forms import formset_factory
from django.forms import modelformset_factory
from Article.forms import *
from Article.models import *
from django.views.generic import *
import datetime
from django.core.paginator import *
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import *

def get_page(request):
	article_list = New_Article.objects.all().order_by('-id')
	paginator = Paginator(article_list,4)
	try:
		page = request.GET.get('page')
		get_page = paginator.page(page)	   		
	except PageNotAnInteger:
		get_page = paginator.page(1)
	except EmptyPage:
		get_page = paginator.page(paginator.num_pages)		
	return get_page		

class article(FormView):
	template_name = 'article.html'
	form_class = MyArticle

	def form_valid(self,form):
		form.save()
		return super(article,self).form_valid(form)


	def get_context_data(self,*args,**kwargs):
		context = super(article,self).get_context_data(*args,**kwargs)
		context['key'] = 'Create'
		return context


	def get_success_url(self):
		return reverse('display_article')

class display_article(ListView):
	template_name = "article_list.html"	
	model = New_Article
	context_object_name = 'article'
	paginate_by = 4

	def get_context_data(self,*args,**kwargs):
		context = super(display_article,self).get_context_data(*args,**kwargs)
		context['page'] = get_page(self.request)
		return context

class article_detail(DetailView):
	template_name = "article_detail.html"
	model = New_Article	
	context_object_name = 'article'


class article_update(UpdateView):
	template_name = "article.html"
	model = New_Article
	form_class = MyArticle
	context_object_name = 'article'


	def get_success_url(self):
		return reverse('display_article')

	def get_context_data(self,*args,**kwargs):
		context = super(article_update,self).get_context_data(*args,**kwargs)
		context['key'] = 'Update'
		return context

class article_delete(DeleteView):
	template_name = "delete.html"
	model = New_Article	
	context_object_name = 'article'	


	def get_success_url(self):
		return reverse('display_article')

	