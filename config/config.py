import os
from os import path

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$7#%0@ufbnnp2ovpt0x-ehcv_g+^yo!0tic6#=fuxz0!4l4(#l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': path.join(path.dirname(path.dirname(__file__)), 'db.sqlite3'),
    }
}