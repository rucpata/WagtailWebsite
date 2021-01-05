from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0qjdxh8nibnbihjuj9*-%$#kx!i8y^wk6wt(h)@27m1g-9g$)v'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['localhost', 'rocketman.naukawagtail.com', ] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


INSTALLED_APPS += [
    'debug_toolbar',
]
MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = [
    '127.0.0.1',
]


try:
    from .local import *
except ImportError:
    pass
