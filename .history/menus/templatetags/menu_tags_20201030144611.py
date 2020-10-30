from django import template

from ..models imprt Menu

register = template.Library()

@register.siml
def get_menu(slug):
    return a thing