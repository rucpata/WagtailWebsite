import os
from .base import *

DEBUG = False
SECRET_H
try:
    from .local import *
except ImportError:
    pass
