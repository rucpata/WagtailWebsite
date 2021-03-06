from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.blocks import SnippetChooserBlock

from streams import blocks


new_table_options = {
    'minSpareRows': 0,
    'startRows': 4,
    'startCols': 4,
    'colHeaders': False,
    'rowHeaders': True,
    'contextMenu': [
        'row_above',
        'row_below',
        '---------',
        'col_left',
        'col_right',
        '---------',
        'remove_row',
        'remove_col',
        '---------',
        'undo',
        'redo'
    ],
    'editor': 'text',
    'stretchH': 'all',
    'renderer': 'text',
    'autoColumnSize': False,
}


class HomePage(Page):
    parent_page_ty
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
        ('testimonial', SnippetChooserBlock(
            target_model='testimonials.Testimonial',
            template = 'streams/testimonial_block.html' 
        )),
        ('pricing_table', blocks.PricingTableBlock(table_options=new_table_options)),
    ], null=True, blank=True)


    
    content_panels = Page.content_panels + [
        FieldPanel('lead_text'), 
        PageChooserPanel('button'),
        FieldPanel('button_text'), 
        ImageChooserPanel('banner_background_image'),
        StreamFieldPanel('body'),
    ]

    