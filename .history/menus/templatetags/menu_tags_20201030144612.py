from django import template

from ..models imprt Menu

register = template.Library()

@register.simle
def get_menu(slug):
    return a thing