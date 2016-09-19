from django.contrib.auth.decorators import login_required,user_passes_test
from django.views.generic.base import TemplateView
from django.views.generic import ListView,DetailView
from django.http import *
from django.template.loader import *
from django.template import *
from django.shortcuts import *
from student.forms import *
from django.forms import formset_factory
from student.models import *
from django.utils import timezone
from django.views.generic import *
from django.core.urlresolvers import *
from django.core.paginator import *
now = timezone.now()
from django.db.models import Q

def get_page(request):
	student_list = Registration.objects.all().order_by('-id')
	paginator = Paginator(student_list,4)
	try:
		page = request.GET.get('page')
		get_page = paginator.page(page)	   		
	except PageNotAnInteger:
		get_page = paginator.page(1)
	except EmptyPage:
		get_page = paginator.page(paginator.num_pages)		
	return get_page		


class registration(FormView):
	template_name = 'registration.html'
	form_class = RegistrationForm


	def form_valid(self,form):
		form.save()
		return super(registration,self).form_valid(form)
	
	def get_success_url(self):
		return reverse('registration')		

class registered_list(ListView):	
	template_name = 'registration_list.html'
	context_object_name = 'objects'
	paginate_by = 4

	def get_context_data(self,**kwargs):
		context = super(registered_list,self).get_context_data(**kwargs)
		context['name_count'] = Registration.name_count.all()
		context['men'] = Registration.men.all()
		context['women'] = Registration.women.all()	
		context['page'] = get_page(self.request)	
		return context

	def get_queryset(self):					
		try:
			q = self.request.GET['q']			
			page = Registration.objects.filter(Q(first_name__icontains = q)|
												Q(last_name__icontains = q)|
												Q(father_name__icontains = q)|
												Q(mother_name__icontains = q)|
												Q(faith_home__icontains = q))					
		except:		
			page = Registration.objects.all().order_by('-id')
		return page	
		

class student_detail(DetailView):
	template_name = 'register_detail.html'
	model = Registration		
	context_object_name = 'student'