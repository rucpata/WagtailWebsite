from django import template

from ..models import Menu

register = template.Library()

from django.shortcuts import render
'''
@register.simple_tag()
def get_menu(slug):
    try: 
        return Menu.objects.get(slug=slug)
    except Menu.DoesNotExist:
        return Menu.objects.none()
'''
@register.simple_tag()
def get_menu(slug):
    all_objects = Menu.objects.all()
    return print(all_objects)

get_menu()