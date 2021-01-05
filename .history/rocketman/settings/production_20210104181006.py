import os
from .base import *

DEBUG = False
SECRET_KEY = ''
ALLOWED_HOSTS ['']
c
try:
    from .local import *
except ImportError:
    pass
