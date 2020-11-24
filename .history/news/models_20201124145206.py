from django.db import models

from modelcluster.models import ParentalKey

from wagtail.contrib.forms.models import AbstractEmailForm
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel 
from wagtail.images.edit_handlers import  ImageChooserPanefrom wa
# Create your models here.

class FormField(AbstractEmailForm):
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
    map_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        help_text='Obrazek będzie przycięty do rozmairu 588px na 355 px',
        related_name='+',
    )
    map_url = models.URLField(
        blank=True,
        help_text='Opcjonalne. Jeśli podasz tutaj łączę, obraz stanie się łączem.'
    )

    content_panels = AbstractEmailForm.content_panel + [
        FieldPanel('intro'),
        ImageChooserPanel('map_iamge'),
        FieldPanel('map_url'),
        InlinePanel('form_fields', label="Form Fields"), 
        FieldPanel('thank_you_text'),
        FieldPanel('from_address'),
        FieldPanel('to_address'),
        FieldPanel('subject'),
        
    ]
     