import os
from .base import *

DEBUG = False
SECRET_KEY = ''
ALLOWED

try:
    from .local import *
except ImportError:
    pass
