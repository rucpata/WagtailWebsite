from django.db import models

from modelcluster.models import ClusterableModel

# Create your models here.
class Menu(ClusterableModel):
    
    title = models.CharField(max_len)
    slug = 
