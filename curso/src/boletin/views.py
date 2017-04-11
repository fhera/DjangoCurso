# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import RegForm
from .models import Registrado

# Create your views here.
def inicio(request):
    form = RegForm(request.POST or None)
    # print(dir(form)) # Muestra todas las opciones de form en la terminal
    if form.is_valid():
        titulo = "HOLA"
        form_data=  form.cleaned_data
        abc = form_data.get("email")
        abc2 = form_data.get("nombre")
        # Con lo siguiente registramos un objeto en bd aunque no es lo que se debería hacer.
        obj = Registrado.objects.create(email=abc, nombre= abc2)

        # De esta forma tb podemos registrar un objeto.
        # obj = Registrado()
        # obj.email = abc
        # obj.save()
    context ={
        "titulo": titulo,
        "el_form": form,
    }
    return render(request,"inicio.html",context)