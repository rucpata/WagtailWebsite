import os
from .base import *

DEBUG = False
SECRET_KEY = []
try:
    from .local import *
except ImportError:
    pass
