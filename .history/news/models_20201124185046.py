from django.db import models

from modelcluster.models import ParentalKey

from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel 
from wagtail.images.edit_handlers import  ImageChooserPanel
from wagtail.core.fields import RichTextField 
# Create your models here.

class FormField(AbstractFormField):
    page = ParentalKey(
        'NewsPage',
        on_delete=models.CASCADE,
        related_name='form_fields',
    )

class NewsPage(AbstractEmailForm):  
    tempalte ='news/news_page.html'
    leanding_page_template = 'news/news_page_leading.html'
    subpage_types = []
    max_coun = 1

    intro = RichTextField(blank=True, features=['bold', 'italic', 'ol', 'ul'])
    thank_you_text = RichTextField(
        blank=True, 
        features=['bold', 'italic', 'ol', 'ul'])
   

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro'),
        ImageChooserPanel('map_image'),
        FieldPanel('map_url'),
        InlinePanel('form_fields', label="Form Fields"), 
        FieldPanel('thank_you_text'),
        FieldPanel('from_address'),
        FieldPanel('to_address'),
        FieldPanel('subject'),
        
    ]
     