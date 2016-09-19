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


class display_article(ListView):
	template_name = "article_list.html"	
	model = New_Article
	context_object_name = 'article'
	paginate_by = 4

	def get_context_data(self,*args,**kwargs):
		context = super(display_article,self).get_context_data(*args,**kwargs)
		context['page'] = get_page(self.request)
		return context