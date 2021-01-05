import os
from .base import *

DEBUG = False
SECRET_KEY = ''
ALLOWED_HOSTS ['']
cwd=os.getcwd
try:
    from .local import *
except ImportError:
    pass
