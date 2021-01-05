import os
from .base import *

DEBUG = False
SECU
try:
    from .local import *
except ImportError:
    pass
