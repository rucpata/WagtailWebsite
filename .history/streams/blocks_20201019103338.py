from wagtail.core import blocks

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
        blocks.StuctBlock(
            [
                ('tite', blocks.CharBlock(
                    max_length=100,
                    help_
                ))
            ]

        )

    )
