from .base import *
import isort
DEBUG = False

try:
    from .local import *
except ImportError:
    pass
