from django import forms
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.contrib.table_block.blocks import TableBlock

#Walidacja problemu
from django.core.exceptions import ValidationError
from django.form.utils import ErrorList

class TitleBlock(blocks.StructBlock):
    text = blocks.CharBlock(
        required = True,
        elp_text='Tekst do wyświetlenia',
    )

    class Meta:
        template = 'streams/title_block.html'
        icon = 'edycja'
        label = 'Tytuł'
        help_text = 'Wyśrodkowany tekst do wyświetlenia na stronie.'

class LinkValue(blocks.StructValue):
    """Dodatkowao logika dla lików"""

    def url(self) -> str:
        internal_page = self.get('internal_page')
        external_link = self.get('external_link')
        if internal_page:
            return internal_page.url
        elif external_link:
            return external_link
        return ''



class Link(blocks.StructBlock):
    link_text = blocks.CharBlock(
        max_length=50, 
        default='Więcej szczegółów'
    )
    internal_page = blocks.PageChooserBlock(
        required=False
    )
    external_link = blocks.URLBlock(
        required=False
    )

    class Meta:
        value_class = LinkValue

    def clean(self, value):
        error = {}
        if w:
           errors['field_name'] = ErrorList('your error text hear')

        



class Card(blocks.StructBlock):
    title = blocks.CharBlock(
        max_length=100, 
        help_text = 'Pogrubiony tytuł tej karty. Maksymalnie 100 znaków.'
    )
    text = blocks.TextBlock(
        max_length=255, 
        help_text='Opcjonalny tekst tej karty. Maksymalnie 255 znaków.'
    )
    image = ImageChooserBlock(
        help_text = 'Obraz zostanie automatycznie przycięty o 570 na 370 pikseli'
    )
    link = Link(help_text = 'Wwybierz link')


class CardsBlock(blocks.StructBlock):
    cards = blocks.ListBlock(
        Card()
    )

    class Meta: 
        template = 'streams/card_block.html'
        icon = 'image'
        label = 'Karty standardowe'

class RadioSelectBlock(blocks.ChoiceBlock):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.field.widget = forms.RadioSelect(
            choices=self.field.widget.choices
        )

class ImageAndTextBlock(blocks.StructBlock):
    image = ImageChooserBlock(help_text='Obraz automatycznie przycięty do rozmiaru 786 na 552 px.')
    image_alignment = RadioSelectBlock(
        choices = (
            ('left','Opraz po lewej stronie'),
            ('right', 'Obraz po prawej stronie'),
        ), 
        default = 'left', 
        help_text = 'Obraz po lewej stronie, tekst po prawej lub obraz po prawej stronie tekst po lewej.'
    )
    title = blocks.CharBlock(
        max_length=60, 
        help_text='Maksymalna długość 60 znaków.'
    )
    text = blocks.CharBlock(
        max_length = 140,
        required = False,
    )
    link = Link()

    class Meta:
        template = 'streams/image_and_text_block.html'
        icon = 'image'
        label = 'Obraz & Tekst'

class CallToActionBlock(blocks.StructBlock):

    title =blocks.CharBlock(
        max_length = 200,
        help_text = 'Maksymalnie 200 znaków.'
    )
    link = Link()
    
    class Meta:
        template = 'streams/call_to_action_block.html'
        icon = 'plus'
        label = 'Wezwanie do działania'

class PricingTableBlock(TableBlock):
    """Blok tabeli cen."""

    class Meta:
        template = 'streams/pricing_table_block.html'
        label = 'Tabela cen'
        icon = 'table'
        help_text = 'Twoje tabele z cenami powinny zawierać zawsze 4 kolumny.'

'''
class RichTextWithTitleBlock(blocks.StructBlock):

    title = blocks.CharBlock(max_length=50)
    context = blocks.RichTextBlock(features=[])

    class Meta:
        template = 'streams/simple_richtext_block.html'
'''