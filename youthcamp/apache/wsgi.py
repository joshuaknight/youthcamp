import os,sys
apache_configuration = os.path.dirname(__file__)
project = os.path.dirname(apache_configuration)
workspace = os.path.dirname(project)
sys.path.append(workspace)
sys.path.append(project)

sys.path.append('/home/joshua/Desktop/projects/youthcamp')

os.environ['DJANGO_SETTINGS_MODULE'] = 'youthcamp.apache.override'

from django.core.wsgi import get_wsgi_application 
application = get_wsgi_application()


