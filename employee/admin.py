from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['s_name', 's_phone', 's_mail', 's_registration', 'd_admission_date','b_in_charge']