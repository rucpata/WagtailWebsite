from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtai
from streams import blocks


class HomePage(Page):
    lead_text = models.CharField(
        max_length = 140, 
        blank = True, 
        help_text = 'Podtytuł pod tytułem banera'
        )

    button = models.ForeignKey(
        'wagtailcore.Page',
        blank = True,
        null = True,
        related_name = '+',
        help_text = 'Wybierz opcjonalną stronę, do której chcesz utworzyć łącze',
        on_delete = models.SET_NULL,
    )

    button_text = models.CharField(
        max_length = 50,
        default = 'Czytaj więcej',
        blank = False,
        help_text = 'Przycisk tekstowy'
    )

    banner_background_image = models.ForeignKey(
        'wagtailimages.Image',
        blank = False,
        null =True,
        related_name = '+',
        help_text = 'Obraz tła baneru',
        on_delete = models.SET_NULL,
    )

    body = StreamField([
        ('title', blocks.TitleBlock()),   
        ('cards', blocks.CardsBlock()),
        ('image_and_text', blocks.ImageAndTextBlock()),
        ('cta', blocks.CallToActionBlock()),
        ('testimonial', SnippetChooserBlock()),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('lead_text'), 
        PageChooserPanel('button'),
        FieldPanel('button_text'), 
        ImageChooserPanel('banner_background_image'),
        StreamFieldPanel('body'),
    ]

    