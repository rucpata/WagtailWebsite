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
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'rocketman',
        'USER': 'rocketman',
        'PASSWORD': 'qwer123',
        'HOST': 'localhost',
        'PORT': '',
    }
}

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://1cb940e033504619a3879ea797658265@o500439.ingest.sentry.io/5580249",
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)

try:
    from .local import *
except ImportError:
    pass
