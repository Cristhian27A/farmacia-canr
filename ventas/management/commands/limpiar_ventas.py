from django.core.management.base import BaseCommand
from ventas.models import DetalleVenta, Venta

class Command(BaseCommand):
    help = 'Elimina todos los registros de ventas y detalles'

    def handle(self, *args, **options):
        # Eliminar todos los detalles de venta
        detalles_count = DetalleVenta.objects.count()
        DetalleVenta.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f'✅ Se eliminaron {detalles_count} detalles de venta.'))
        
        # Eliminar todas las ventas
        ventas_count = Venta.objects.count()
        Venta.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f'✅ Se eliminaron {ventas_count} ventas.'))
        
        self.stdout.write(self.style.SUCCESS('✅ Historial de ventas limpiado completamente.'))
