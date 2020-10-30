from django.db import models

from modelcluster.models import ClusterableModel

# Create your models here.
class Menu(ClusterableModel):
    
    title = models.CharField(max_length=100)
    slug = AutoSlugField(
        populate_from='title',
        
    )
