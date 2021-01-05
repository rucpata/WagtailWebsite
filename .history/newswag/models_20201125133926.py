from django.db import models

# Create your models here.
from wagtailnews.models import AbstractNewsItem, AbstractNewsItemRevision
from wagtail.wagtailcore.fields import RichTextField

class NewsItem(AbstractNewsItem):
    title = models.CharField(max_length=100)
    body = RichTextField()

    panels = [
        FieldPanel('title'),
        FieldPanel('body'),
    ]

    def __str__(self):
        return self.title

# This table is used to store revisions of the news items.
class NewsItemRevision(AbstractNewsItemRevision):
    # This is the only field you need to define on this model.
    # It must be a foreign key to your NewsItem model,
    # be named 'newsitem', and have a related_name='revisions'
    newsitem = models.ForeignKey(NewsItem, related_name='revisions')