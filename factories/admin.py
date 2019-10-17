from django.contrib import admin
from .models import Factories

@admin.register(Factories)
class FactoriesAdmin(admin.ModelAdmin):
    list_display = ['s_name']