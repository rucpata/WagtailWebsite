from django.db import models

from wagtail.contrib.forms.models import AbstractEmailForm

# Create your models here.
class NewsPage(AbstractEmailForm):  
    tempalte ='news/news_page.html'
    leanding_page_template = 'news/news_page_leading.html'
    subpage_types = []
    max_coun = 1

    intro = RichTextField
    thank_you_text = RichTextField
    map_image = FK to wagtail image 
    map_url = URL Fild

    content_panels = AbstractEmailForm.content_panel + [
        FieldPanel('intro'),
        ImageChooserPanel('map_iamge'),
        FieldPanel('map_url'),
        InlinePanel('form_field'),
    ]
     