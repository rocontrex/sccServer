from django.shortcuts import render, redirect
from .models import Factories


def listar_factories(request):
    factories = Factories.objects.all()
    return render(request, '', {'factories': factories})

def criar_factories(request):
    return

def atualizar_factories(request):
    return 

def deletar_factories(request):
    return 