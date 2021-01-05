import os
from .base import *

DEBUG = False
SECRET_KEY = ''
ALLOWED_HOSTS ['']
cwd=os.get
try:
    from .local import *
except ImportError:
    pass
