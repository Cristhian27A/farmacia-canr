from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView
from django.db import models, transaction
from .forms import VentaForm
from .models import Venta, DetalleVenta

def index(request):
    # Obtener todos los detalles de venta ordenados por fecha descendente
    detalles = DetalleVenta.objects.select_related('venta', 'medicamento').order_by('-venta__fecha')
    
    # Calcular total de ventas (cantidad de transacciones)
    total_ventas = Venta.objects.count()
    
    # Calcular ingresos totales (suma de todos los totales de venta)
    ingresos_totales = Venta.objects.aggregate(total=models.Sum('total'))['total'] or 0
    
    context = {
        'detalles': detalles,
        'total_ventas': total_ventas,
        'ingresos_totales': ingresos_totales,
    }
    
    return render(request, 'ventas/index.html', context)

def registrar_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            medicamento = form.cleaned_data['medicamento']
            cantidad = form.cleaned_data['cantidad']
            precio_unitario = medicamento.precio
            subtotal = cantidad * precio_unitario
            
            try:
                with transaction.atomic():
                    # Crear venta
                    venta = Venta.objects.create(total=subtotal)
                    
                    # Crear detalle de venta
                    detalle = DetalleVenta.objects.create(
                        venta=venta,
                        medicamento=medicamento,
                        cantidad=cantidad,
                        precio_unitario=precio_unitario,
                        subtotal=subtotal
                    )
                    
                    # Actualizar stock del medicamento
                    medicamento.stock -= cantidad
                    medicamento.save()
                    
                    messages.success(request, f'Venta registrada exitosamente. Total: ${venta.total}')
                    return redirect('ventas:index')
            except Exception as e:
                messages.error(request, str(e))
    else:
        form = VentaForm()
    
    return render(request, 'ventas/registrar_venta.html', {'form': form})
