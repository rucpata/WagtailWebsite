# Generated by Django 3.1.2 on 2020-10-19 09:04

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_homepage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('title', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(elp_text='Tekst do wyświetlenia', required=True))])), ('cards', wagtail.core.blocks.StructBlock([('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Pogrubiony tytuł tej karty. Maksymalnie 100 znaków.', max_length=100)), ('text', wagtail.core.blocks.TextBlock(help_text='Opcjonalny tekst tej karty. Maksymalnie 255 znaków.', max_length=255)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Obraz zostanie automatycznie przycięty o 570 na 370 pikseli'))])))]))], blank=True, null=True),
        ),
    ]
