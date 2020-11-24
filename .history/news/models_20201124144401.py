from django.db import models

from wagtail.contrib.forms.models import AbstractEmailForm

# Create your models here.
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
    map_url = models.URLField()

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
     