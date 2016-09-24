import os

from conf import email,secret,installed_apps,middle,templates_conf,database,password_validator

EMAIL_BACKEND = email.EMAIL_BACKEND
EMAIL_HOST = email.EMAIL_HOST
EMAIL_HOST_USER = email.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = email.EMAIL_HOST_PASSWORD
EMAIL_PORT = email.EMAIL_PORT
EMAIL_USE_TLS = email.EMAIL_USE_TLS

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = secret.SECRET

DEBUG = True

MARKDOWN_EXTENSIONS = ['extra']

SITE_ID = 1

ALLOWED_HOSTS = []

INSTALLED_APPS = installed_apps.MY_APPS

MIDDLEWARE_CLASSES = middle.MIDDLE_ALL

ROOT_URLCONF = 'youthcamp.urls'

TEMPLATES = templates_conf.MY_TEMPLATE_CONF

WSGI_APPLICATION = 'youthcamp.wsgi.application'

DATABASES = database.DATA

AUTH_PASSWORD_VALIDATORS = password_validator.PASSWORD_AUTH

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'

#STATIC_ROOT = BASE_DIR + '/static'

STATICFILES_FINDERS = ( 
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    '/var/www/static/',
]


MEDIA_ROOT = BASE_DIR + '/static/media'

MEDIA_URL = ''
