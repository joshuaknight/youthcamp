from django.views.generic.base import TemplateView
from django.utils import timezone
#from .models import *
#from .forms import *


class home_page(TemplateView):
	template_name = 'base.html'
	def get_context_data(self, **kwargs):
		context = super(home_page,self).get_context_data( **kwargs)
		context['now'] = timezone.now()
		return context
