from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_factories),
    path('criar', views.criar_factories),
    path('atualizar/<int:id>', views.atualizar_factories),
    path('deletar/<int:id>', views.deletar_factories)
]