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

def get_menu(request):
    all_objects = Menu.objects.all()
    return render(request, 'includes/header.h')

