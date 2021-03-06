from django import template

from ..models import Menu

register = template.Library()

@register.simple_tag()
def get_menu(slug):
    try: 
        wszystko = Menu.objects.get(slug=slug)
        return wszystko.on
    except Menu.DoesNotExist:
        return Menu.objects.none()