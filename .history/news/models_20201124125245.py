from django.db import models

from wagtail.contrib.forms.models import AbstractEmailForm

# Create your models here.
class NewsPage(AbstractEmailForm):  
    tempalte ='news'