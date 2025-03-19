from django.shortcuts import render,redirect
from .models import Materiales

# Create your views here.
def material(request):
    if request.method == 'POST':
        lote = request.POST['lote']
        tipo_material = request.POST['tipo_material']
        descripcion = request.POST['descripcion']
        cantidad = request.POST['cantidad']
        nuevo_material = Materiales(lote=lote, tipo_material=tipo_material, descripcion=descripcion, cantidad=cantidad)
        nuevo_material .save()
        
    return render(request, 'material.html')
   
   
# Vista de la página de inventario
def inventory_view(request):
    materiales = Materiales.objects.all() # Obtenemos todos los materiales
    return render(request, 'inventory.html', {'materiales': materiales})# Pasamos los materiales a la plantilla

# Función para eliminar un material
def delete_material(request, id):
        material = Materiales.objects.get(id=id)# Obtenemos el material por su id
        material.delete()# Eliminamos el material
        return redirect('inventory')# Redirigimos a la página de inventario
    
# Función para editar un material
def edit_material(request, id):
    material = Materiales.objects.get(id=id)# Obtenemos el material por su id
    if request.method == 'POST':# Si se envía un formulario
        material.lote = request.POST['lote']
        material.tipo_material = request.POST['tipo_material']
        material.descripcion = request.POST['descripcion']
        material.cantidad = request.POST['cantidad']
        material.save()# Guardamos el material editado
        return redirect('inventory')# Redirigimos a la página de inventario
    return render(request, 'editar_material.html', {'material': material})# Pasamos el material a la plantilla de edición