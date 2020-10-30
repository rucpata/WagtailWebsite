from django import template

from ..models imprt Menu

register = template.Library()

@register.simple_tag()
def get_menu(slug):
    return 'a thing