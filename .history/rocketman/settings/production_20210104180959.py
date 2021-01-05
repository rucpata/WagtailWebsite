import os
from .base import *

DEBUG = False
SECRET_KEY = ''
ALLOWED_HOSTS 

try:
    from .local import *
except ImportError:
    pass
