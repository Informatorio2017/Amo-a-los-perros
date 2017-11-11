from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Evento
from .forms import EventoForm


def eventos(request):
    eventos = Evento.objects.all()
    contexto = {
        "eventos": eventos,
        "otra_variable": 1,
    }
    return render(request, 'eventos/eventos.html', contexto)


def nuevo(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Evento creado correctamente.')
            return redirect('/eventos')
    else:
        form = EventoForm()
    contexto = {
        "form": form
    }
    return render(request, 'eventos/nuevo.html', contexto)
