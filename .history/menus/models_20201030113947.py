from django.db import models

from django_extensi
from modelcluster.models import ClusterableModel

# Create your models here.
class Menu(ClusterableModel):
    
    title = models.CharField(max_length=100)
    slug = AutoSlugField(
        populate_from='title',
        editable=True,
    )
