from django.contrib import admin
from .models import Teams

@admin.register(Teams)
class TeamsAdmin(admin.ModelAdmin):
    list_display = ['s_name', 'i_indicador']