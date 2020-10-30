from django.db import models
from django.core.exceptions import ValidationError

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class ServiceListingPage(Page):
    parent_page_type = ['home.HomePage']
    tamplate = 'services/service_listing_page.html'
    subtitle = models.TextField(
        blank = True,
        max_length = 500,
    )
    
    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
    ]

    def get_context(self, request,*args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['services'] =  ServicePage.objects.live().public()
        return context


class ServicePage(Page):
    
    tamplate = 'services/service_page.html'
    description = models.TextField(
        blank = True,
        max_length = 500,
    )

    internal_page = models.ForeignKey(
        'wagtailcore.Page',
        blank = True,
        null = True, 
        related_name = '+',
        help_text = ' Wybierz wewnętrzną stronę Wegtail',
        on_delete = models.SET_NULL,
    )

    external_page = models.URLField(
        blank = True, 
    )

    button_text =models.CharField(
        blank = True,
        max_length = 50,
    )

    service_image = models.ForeignKey(
        'wagtailimages.Image',
        null = True,
        blank = False,
        on_delete = models.SET_NULL,
        help_text = 'Ten obraz zostanie użyty na stronie z wykazem usług i zostanie przycięty do rozmiaru 570 na 370 pikseli na tej stronie.',
        related_name = '+',
    )
    
    content_panels = Page.content_panels + [
        FieldPanel('description'),
        PageChooserPanel('internal_page'),
        FieldPanel('external_page'),
        FieldPanel('button_text'), 
        ImageChooserPanel('service_image'),
    ]

    def clean(self):
        super().clean()

        if self.internal_page and self.external_page:
            #Both firlds are filled out 
            raise ValidationError({
                'internal_page': ValidationError('Wybierz tylko stronę LUB wprowadź zewnętrzny adres URL'),
                'external_page': ValidationError('Wybierz tylko stronę LUB wprowadź zewnętrzny adres URL')
            })
        #if something:
            #cause an error
        if not self.internal_page and not self.external_page:
            raise ValidationError({
                'internal_page': ValidationError('Musisz wybrać stronę LUB wpisać zewnętrzny adres URL'),
                'external_page': ValidationError('Musisz wybrać stronę LUB wpisać zewnętrzny adres URL'),
        })