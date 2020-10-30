from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core import blocks as wagtail_blocks

from streams import blocks
from home.models import new_table_options



class FlexPage(Page):
    parent_page_type = ["home.HomePage", "flexF"]
    body = StreamField([
        ('title', blocks.TitleBlock()),   
        ('cards', blocks.CardsBlock()),
        ('image_and_text', blocks.ImageAndTextBlock()),
        ('cta', blocks.CallToActionBlock()),
        ('testimonial', SnippetChooserBlock(
            target_model='testimonials.Testimonial',
            template = 'streams/testimonial_block.html' 
        )),
        ('pricing_table', blocks.PricingTableBlock(
            table_options=new_table_options,
        )),
        ('richtext', wagtail_blocks.RichTextBlock(
            template = 'streams/simple_richtext_block.html',
            features = ['bold', 'italic', 'ol', 'ul', 'link']
        )),
        ('large_image', ImageChooserBlock(
            help_text = 'Ten obraz będzie przycięty do 1200px na 775px',
            template='streams/large_image_block.html'
        ))
    
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    class Meta:
        verbose_name = 'Flex (misc) page'
        verbose_name_plural = 'Flex (misc) pages'