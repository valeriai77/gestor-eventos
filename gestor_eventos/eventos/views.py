from django.shortcuts import render, redirect, get_object_or_404
from .models import Evento, Participante
from .forms import EventoForm, ParticipanteForm

def inicio(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/inicio.html', {
        'eventos': eventos
    })

def lista_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/lista_eventos.html', {'eventos': eventos})

def crear_evento(request):
    form = EventoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('lista_eventos')
    return render(request, 'eventos/form_evento.html', {'form': form})

def editar_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    form = EventoForm(request.POST or None, request.FILES or None, instance=evento)
    if form.is_valid():
        form.save()
        return redirect('lista_eventos')
    return render(request, 'eventos/form_evento.html', {'form': form})

def eliminar_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    evento.delete()
    return redirect('lista_eventos')

def lista_participantes(request):
    participantes = Participante.objects.all()
    return render(request, 'eventos/lista_participantes.html', {'participantes': participantes})

def crear_participante(request):
    form = ParticipanteForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('lista_participantes')
    return render(request, 'eventos/form_participante.html', {'form': form})

def editar_participante(request, id):
    participante = get_object_or_404(Participante, id=id)
    form = ParticipanteForm(request.POST or None, request.FILES or None, instance=participante)
    if form.is_valid():
        form.save()
        return redirect('lista_participantes')
    return render(request, 'eventos/form_participante.html', {'form': form})

def eliminar_participante(request, id):
    participante = get_object_or_404(Participante, id=id)
    participante.delete()
    return redirect('lista_participantes')