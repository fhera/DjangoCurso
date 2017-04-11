# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Registrado
from .forms import RegModelForm
# Register your models here.

class AdminRegistrado(admin.ModelAdmin):
    list_display = ["email", "nombre", "timestamp"]
    form = RegModelForm
    # list_filter = ["timestamp"]
    list_editable = ["nombre"]
    search_fields = ["email", "nombre", "email"]

    # Si queremos añadir desde las vistas objetos a la bd.
    # class Meta:
    #     model = Registrado

admin.site.register(Registrado, AdminRegistrado)