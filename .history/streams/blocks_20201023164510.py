from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


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
    interal_page = blocks.PageChooserBlock(
        required=False
    )
    external_link = blocks.URLBlock(
        required=False
    )

    class Meta:
        value_class = LinkValue


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

class ImageAndTextBlock(blocks.StructBlock):
    image = ImageChooserBlock(help_text='Obraz ')
    image_alignment
    title 
    text 
    link - Link()