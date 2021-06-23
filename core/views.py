from django.http import response
from django.shortcuts import redirect, render

from core.models import cancion
from .forms import *
def home(request):    
    return render(request, 'index.html', {})


def ListarCanciones(request):
    canciones = cancion.objects.all()
    context = {'canciones': canciones}
    return render(request, 'listarcanciones.html', context)


def CrearCancion(request):
    if request.method == "POST":
        form = CancionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar')
    elif request.method == "GET":
        form = CancionForm()
    context = {'form': form.as_p}
    return render(request, 'crearcancion.html', context)


def EliminarCancion(request, id_cancion):
    cancionEliminar = cancion.objects.get(id=id_cancion)
    cancionEliminar.delete()
    return redirect('listar')


def EditarCancion(request, id_cancion):
    cancionEditar = cancion.objects.get(id=id_cancion)
    if request.method == "POST":
        form = CancionForm(request.POST, instance=cancionEditar)
        if form.is_valid():
            form.save()
            return redirect('home')

    elif request.method == "GET":
        form = CancionForm(instance=cancionEditar)
    context = {'form': form.as_p}
    return render(request, 'editarcancion.html', context)


def VerInfor(request, id_cancion):
    cancionInfo = cancion.objects.get(id=id_cancion)
    context = {'cancion': cancionInfo}
    return render(request, 'informacion.html', context)