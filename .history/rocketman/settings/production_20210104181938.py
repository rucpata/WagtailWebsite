import os
from .base import *

DEBUG = False
SECRET_KEY = '$^8&x#8a5!7@r!#6ov9bfl(j8k^6+$v-1x+*#!uqf(=^n+*$w3'
ALLOWED_HOSTS = ['localhost', 'rocketman.naukawagtail.com', '*']
cwd=os.getcwd()

CASHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': f"{cwd}/.cache"
    }
}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'USER': ''
    }
}


try:
    from .local import *
except ImportError:
    pass
