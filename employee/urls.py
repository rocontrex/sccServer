from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_employee),
    path('criar', views.criar_employee),
    path('atualizar/<int:id>', views.atualizar_employee),
    path('deletar/<int:id>', views.deletar_employee)
]