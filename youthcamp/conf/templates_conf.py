import os 

#BASE_DIR = '/home/joshua/Desktop/youthcamp/'
BASE_DIR = os.path.dirname(os.path.abspath('s'))


MY_TEMPLATE_CONF  = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR + '/Feedback/template',
                BASE_DIR + '/youthcamp/templates',
                BASE_DIR + '/contact/template',
                BASE_DIR + '/student/template',
                BASE_DIR + '/Article/template',
                BASE_DIR + '/Login/template',],

        #'/template',
         #       '/home/joshua/Desktop/youthcamp/template',],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]