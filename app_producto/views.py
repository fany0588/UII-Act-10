from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Producto
from .forms import ProductoForm


# Create your views here.
def index_productos(request):
	return render(request, 'productos/index.html', {
		'productos': Producto.objects.all()
	})


def view_producto(request, id):
	# Redirigir a la vista de índice, ya que la información detallada está en el modal de index.html
	return HttpResponseRedirect(reverse('index'))


def add_producto(request):
	if request.method == 'POST':
		form = ProductoForm(request.POST)
		if form.is_valid():
			# No necesitamos extraer campo por campo, form.save() lo hace por nosotros
			form.save()
			return render(request, 'productos/add.html', {
				'form': ProductoForm(),
				'success': True
			})
	else:
		form = ProductoForm()
	return render(request, 'productos/add.html', {
		'form': form
	})


def edit_producto(request, id):
	producto = get_object_or_404(Producto, pk=id) # Usa get_object_or_404 para manejar si el ID no existe
	if request.method == 'POST':
		form = ProductoForm(request.POST, instance=producto)
		if form.is_valid():
			form.save()
			return render(request, 'productos/edit.html', {
				'form': form,
				'success': True,
				'producto': producto # Pasar el objeto producto también
			})
	else:
		form = ProductoForm(instance=producto)
	return render(request, 'productos/edit.html', {
		'form': form,
		'producto': producto # Pasar el objeto producto también
	})


def delete_producto(request, id):
	if request.method == 'POST':
		producto = get_object_or_404(Producto, pk=id) # Usa get_object_or_404
		producto.delete()
	return HttpResponseRedirect(reverse('index')) 