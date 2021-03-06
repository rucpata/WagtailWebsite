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


class CardsBlock(blocks.StructBlock):
    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('title', blocks.CharBlock(max_length=100, help_text = 'Pogrubiony tytuł tej karty. Maksymalnie 100 znaków.')),
                ('text', blocks.TextBlock(max_length=255, help_text='Opcjonalny tekst tej karty. Maksymalnie 255 znaków.')),
                ('image', ImageChooserBlock(help_text = 'Obraz zostanie automatycznie przycięty o 570 na 370 pikseli')),
                ('link_text', blocks.CharBlock(max_length=50, de)),
                ('interal_page', blocks.PageChooserBlock(required=False)),
                ('internal_link', blocks.URLBlock(required=False))
            ]
        )
    )
    class Meta: 
        template = 'streams/card_block.html'
        icon = 'image'
        label = 'Karty standardowe'
