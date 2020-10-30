from django import template

from ..models imprt Menu

register = template.Library()

@register
def get_menu(slug):
    return a thing