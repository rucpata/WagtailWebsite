""" Kategoria zostanie dodana w pasku bocznym u admina"""
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from .models import Meny

class MenuAdmin(ModelAdmin)
model = Menu