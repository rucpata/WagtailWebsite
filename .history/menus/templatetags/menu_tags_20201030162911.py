from django import template

from ..models import Menu

register = template.Library()


'''
@register.simple_tag()
def get_menu(slug):
    try: 
        return Menu.objects.get(slug=slug)
    except Menu.DoesNotExist:
        return Menu.objects.none()
'''

from django.shortcuts import render
from django.utils import timezone

from ..models import Menu
@register.simple_tag()
def get_menu(slug):
    all_objects = Menu.objects.all()
    return print(all_objects)

get_menu()