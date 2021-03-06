from django.db import models

from django_extensions.db.fields import AutoSlugField
from modelcluster.models import ClusterableModel

from wagtail.core.models import Orderable 
from wagtail.admin.edit_handlers import FieldPanel

class MenuItem(Orderable):
    link_title = models.CharField(blank=True, nul)
    link_url = external_link
    link_page = internal_link
    open_in_new_tab



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

    def __str__(self):
        return self.title
