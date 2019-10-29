from django import forms
from.models import Employee

class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields = [
            's_name',
            's_phone',
            's_mail',
            's_registration',
            'd_admission_date',
            'b_in_charge',
            'b_has_team',
            'r_user'
        ]