from django.db import models


from django_extensions.db.fields import AutoSlugField
from modelcluster.models import ClusterableModel

from wagtail.admin.edit_handlers import FieldPanel


class Menu(ClusterableModel):
    
    title = models.CharField(max_length=100)
    slug = AutoSlugField(
        populate_from='title',
        editable=True,
    )

    panels = [
        FieldPanel('title'),
        FieldPanel('slug'),
    ]

    <x-12
