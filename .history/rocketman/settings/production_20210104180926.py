import os
from .base import *

DEBUG = False
SEC
try:
    from .local import *
except ImportError:
    pass
