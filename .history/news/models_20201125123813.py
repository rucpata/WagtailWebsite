from django.db import models
from django.u

from modelcluster.models import ParentalKey

from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel 
from wagtail.images.edit_handlers import  ImageChooserPanel
from wagtail.core.fields import RichTextField 
# Create your models here.

FORM_FIELD_CHOICES = (
    ('singleline', _('Single line text')),
    ('multiline', _('Multi-line text')),
    ('email', _('Email')),
    ('url', _('URL')),
)

class CustomAbstractFormField(AbstractFormField):
    field_type = models.CharField(
        vebose_name= 'Field Type',
        max_length = 16,
        choices = FORM_FIELD_CHOICES,
    )

class FormField(AbstractFormField):
    page = ParentalKey(
        'NewsPage',
        on_delete=models.CASCADE,
        related_name='form_fields',
    )

    class Meta:
        abstract = True
        ordering = ['sort_order']

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
     