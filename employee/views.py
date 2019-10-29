from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm


def list_employee(request):
    employee = Employee.objects.all()
    return render(request, '', {'employee': employee})

def create_employee(request):
    form = EmployeeForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('list_employee')
    
    return render(request, '', {'form': form})

def update_employee(request):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST or None, instance=employee)

    if form.is_valid():
        form.save()
        return redirect(request, '', {'form': form})

    return render(request, '', {'form': form, 'employee': employee})

def delete_employee(request):
    employee = Employee.objects.get(id=id)

    if request.method == 'POST':
        employee.delete()
        return redirect('list_employee')

    return render(request, '', {'employee':employee})