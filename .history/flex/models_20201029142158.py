from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

class FlexPage(Page):

    body = StreamField([
        ('title', blocks.TitleBlock()),   
        ('cards', blocks.CardsBlock()),
        ('image_and_text', blocks.ImageAndTextBlock()),
        ('cta', blocks.CallToActionBlock()),
        ('testimonial', SnippetChooserBlock(
            target_model='testimonials.Testimonial',
            template = 'streams/testimonial_block.html' 
        )),
        ('pricing_table', blocks.PricingTableBlock(table_options=new_table_options)),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [

    ]
    
    class Meta:
        verbose_name = 'Flex (misc) page'
        verbose_name_plural = 'Flex (misc) pages'