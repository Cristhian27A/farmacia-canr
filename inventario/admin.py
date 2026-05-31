from django.contrib import admin
from .models import Medicamento, Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_creacion')
    search_fields = ('nombre', 'descripcion')
    readonly_fields = ('fecha_creacion',)

@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'stock', 'fecha_vencimiento', 'fecha_registro')
    list_filter = ('categoria', 'fecha_vencimiento', 'fecha_registro')
    search_fields = ('nombre', 'descripcion')
    readonly_fields = ('fecha_registro',)
