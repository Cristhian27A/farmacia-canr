#!/usr/bin/env python
"""
Script para limpiar registros de ventas de medicamentos eliminados
Ejecutar dentro de: python manage.py shell
Luego copiar y pegar el contenido de este script
"""

from ventas.models import DetalleVenta, Venta

# Identificar registros de ventas donde medicamento es None (productos eliminados)
ventas_sin_medicamento = DetalleVenta.objects.filter(medicamento__isnull=True)

print(f"Se encontraron {ventas_sin_medicamento.count()} registros de ventas de productos eliminados")

if ventas_sin_medicamento.exists():
    print("\nDetalles de registros a eliminar:")
    for detalle in ventas_sin_medicamento:
        print(f"  - DetalleVenta ID: {detalle.id}, Cantidad: {detalle.cantidad}, Subtotal: ${detalle.subtotal}")
    
    # Eliminar los registros de ventas de productos eliminados
    eliminados = ventas_sin_medicamento.delete()[0]
    print(f"\n✅ Se eliminaron {eliminados} registros de ventas de productos eliminados exitosamente.")
    
    # Limpiar ventas vacías (ventas que no tienen detalles)
    ventas_vacias = Venta.objects.filter(detalles__isnull=True)
    if ventas_vacias.exists():
        ventas_eliminadas = ventas_vacias.delete()[0]
        print(f"✅ Se eliminaron {ventas_eliminadas} ventas vacías.")
else:
    print("✅ No se encontraron registros de ventas de productos eliminados.")
