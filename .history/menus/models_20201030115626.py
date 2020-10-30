from django.db import models

from django_extensions.db.fields import AutoSlugField
from modelcluster.models import ClusterableModel

from wagtail.core.models import Orderable 
from wagtail.admin.edit_handlers import FieldPanel

class MenuItem(Orderable):
    link_title = models.CharField(blank=True, max_length=50)
    link_url = models.CharField(max_length=500, blank=True)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+',
        on_delete=models.CASDACE,
    )
    open_in_new_tab = models.BooleanField(
        default=False,
        
    )



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
