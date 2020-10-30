""" Kategoria zostanie dodana w pasku bocznym u admina"""
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from .models import Menu

class MenuAdmin(ModelAdmin):
    model = Menu
    menu_lable = 'Menus'
    menu_icon = 'list-ul'
    menu_o