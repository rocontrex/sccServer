from django.shortcuts import render, redirect
from .models import Employee


def listar_employee(request):
    employee = Employee.objects.all()
    return render(request, '', {'employee': employee})

def criar_employee(request):
    return

def atualizar_employee(request):
    return

def deletar_employee(request):
    return