""" Kategoria zostanie dodana w pasku bocznym u admina"""
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from .models

class MenuAdmin(ModelAdmin)
model = Menu