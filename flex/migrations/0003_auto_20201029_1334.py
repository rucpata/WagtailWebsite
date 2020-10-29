# Generated by Django 3.1.2 on 2020-10-29 13:34

from django.db import migrations
import streams.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0002_flexpage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='body',
            field=wagtail.core.fields.StreamField([('title', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(elp_text='Tekst do wyświetlenia', required=True))])), ('cards', wagtail.core.blocks.StructBlock([('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Pogrubiony tytuł tej karty. Maksymalnie 100 znaków.', max_length=100)), ('text', wagtail.core.blocks.TextBlock(help_text='Opcjonalny tekst tej karty. Maksymalnie 255 znaków.', max_length=255)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Obraz zostanie automatycznie przycięty o 570 na 370 pikseli')), ('link', wagtail.core.blocks.StructBlock([('link_text', wagtail.core.blocks.CharBlock(default='Więcej szczegółów', max_length=50)), ('internal_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False))], help_text='Wwybierz link'))])))])), ('image_and_text', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='Obraz automatycznie przycięty do rozmiaru 786 na 552 px.')), ('image_alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Opraz po lewej stronie'), ('right', 'Obraz po prawej stronie')], help_text='Obraz po lewej stronie, tekst po prawej lub obraz po prawej stronie tekst po lewej.')), ('title', wagtail.core.blocks.CharBlock(help_text='Maksymalna długość 60 znaków.', max_length=60)), ('text', wagtail.core.blocks.CharBlock(max_length=140, required=False)), ('link', wagtail.core.blocks.StructBlock([('link_text', wagtail.core.blocks.CharBlock(default='Więcej szczegółów', max_length=50)), ('internal_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False))]))])), ('cta', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Maksymalnie 200 znaków.', max_length=200)), ('link', wagtail.core.blocks.StructBlock([('link_text', wagtail.core.blocks.CharBlock(default='Więcej szczegółów', max_length=50)), ('internal_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False))]))])), ('testimonial', wagtail.snippets.blocks.SnippetChooserBlock(target_model='testimonials.Testimonial', template='streams/testimonial_block.html')), ('pricing_table', streams.blocks.PricingTableBlock(table_options={'autoColumnSize': False, 'colHeaders': False, 'contextMenu': ['row_above', 'row_below', '---------', 'col_left', 'col_right', '---------', 'remove_row', 'remove_col', '---------', 'undo', 'redo'], 'editor': 'text', 'minSpareRows': 0, 'renderer': 'text', 'rowHeaders': True, 'startCols': 4, 'startRows': 4, 'stretchH': 'all'})), ('richtext', wagtail.core.blocks.RichTextBlock())], blank=True, null=True),
        ),
    ]