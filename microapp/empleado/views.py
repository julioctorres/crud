from django.shortcuts import render, redirect
from .models import empleado
# Create your views here.

def listar_empleados(request):
    Empleado = empleado.objects.all()
    return render(request, 'empl.html', {"Empleado": Empleado})

def create_emp(request):
    empleados = empleado(codigo=request.POST['codigo'], 
            nif=request.POST['nif'], 
            nombre=request.POST['nombre'], 
            apellido_1=request.POST['apellido_1'],
            apellid_2=request.POST['apellid_2'],
            codigo_departamento=request.POST['codigo_departamento'])
    empleados.save()
    print(request.POST)
    return redirect('/empleados/')

def delete_empleados(request, id):
    empleados = empleado.objects.get(id=id)
    empleados.delete()
    return redirect('/empleados/')

def editar_empleados(request, id):
    empleados = empleado.objects.get(id=id)
    empleados = empleado(codigo=request.get['codigo'], 
            nif=request.get['nif'], 
            nombre=request.get['nombre'], 
            apellido_1=request.get['apellido_1'],
            apellid_2=request.get['apellid_2'],
            codigo_departamento=request.get['codigo_departamento'])
    empleados.save()
    return redirect('/empleados/')

