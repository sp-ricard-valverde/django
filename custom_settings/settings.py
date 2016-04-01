from django.conf.global_settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dev_django',
        'USER': 'django_developer',
        'PASSWORD': 'django_developer',
        'HOST': '127.0.0.1',
        'PORT': '',
    },

    'other': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dev_other_django',
        'USER': 'django_developer',
        'PASSWORD': 'django_developer',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}

SECRET_KEY = '_jm6o3ujb#bm-t7dbewa4xeu5+(dm^po8el82jz2nyjk42odfh'
