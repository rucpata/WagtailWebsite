from wagtail.core import blocks

class TitleBlock(blocks.StructBlock):
    streams
    text = blocks.CharBlock(
        required = True,
        elp_text='Tekst do wyświetlenia',
    )
    class Meta:
        template = ''
        icon = ''
        label = ''
        help_text = ''