from wagtail.core import blocks

class TitleBlock(blocks.StructBlock):
    text = blocks.CharBlock(
        required = True,
help_text='Tekst do  '

    )