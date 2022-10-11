from django.urls import path
from .views import listar_empleados, create_emp, delete_empleados, editar_empleados

urlpatterns = [
    path('', listar_empleados), 
    path('new/', create_emp),
    path('delete/<int:id>/', delete_empleados, name='delete'),
    path('editar/<int:id>/', editar_empleados, name='editar')

]
