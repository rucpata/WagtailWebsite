import os
from .base import *

DEBUG = False
SECRET_KEY = '$^8&x#8a5!7@r!#6ov9bfl(j8k^6+$v-1x+*#!uqf(=^n+*$w3'
ASLLOWED_HOST ['']
cwd=os.getcwd()
try:
    from .local import *
except ImportError:
    pass
