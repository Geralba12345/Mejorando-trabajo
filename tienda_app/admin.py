from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Tienda

@admin.register(Tienda)
class TiendaAdmin(ModelAdmin):
    ...

