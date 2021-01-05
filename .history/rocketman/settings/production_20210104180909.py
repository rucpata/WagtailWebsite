from .base import *
impor
DEBUG = False

try:
    from .local import *
except ImportError:
    pass
