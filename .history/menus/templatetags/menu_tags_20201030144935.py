from django import template

from ..models imoprt Menu

register = template.Library()

@register.simple_tag()
def get_menu(slug):
    return 'a thing'