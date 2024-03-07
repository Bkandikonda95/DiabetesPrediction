import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES_DIR = os.path.join(BASE_DIR,'templates')
STATIC_URL = '/static/'

ROOT_URLCONF = 'PycharmProjectsDiabetesprediction.urls'

# Define the directories from which to collect static files
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Define the directory where static files will be collected during deployment
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Define installed apps
INSTALLED_APPS = [
    # other installed apps...
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.messages',

]
MIDDLEWARE = [
    # Other middleware...
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Other middleware...
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['C:/Users/BKand/PycharmProjectsDiabetesprediction/PycharmProjectsDiabetesprediction/templates'],

        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # Add this line
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

SECRET_KEY = "HARISH"

DEBUG = True

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
