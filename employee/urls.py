from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_employee),
    path('create', views.create_employee),
    path('update/<int:id>', views.update_employee),
    path('delete/<int:id>', views.delete_employee)
]