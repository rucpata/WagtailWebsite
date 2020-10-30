from django import template

from ..models import Menu

register = template.Library()

@register.simple_tag()
def get_menu(slug):
    try: 
        wszystko = 
        return list(wszystko)
    except Menu.DoesNotExist:
        return Menu.objects.none()