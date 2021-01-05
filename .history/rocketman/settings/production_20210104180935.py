import os
from .base import *

DEBUG = False
SECRET
try:
    from .local import *
except ImportError:
    pass
