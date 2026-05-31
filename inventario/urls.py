from django.urls import path
from . import views

app_name = 'inventario'

urlpatterns = [
    path('', views.MedicamentoListView.as_view(), name='lista_medicamentos'),
    path('crear/', views.MedicamentoCreateView.as_view(), name='crear_medicamento'),
    path('editar/<int:pk>/', views.MedicamentoUpdateView.as_view(), name='editar_medicamento'),
    path('eliminar/<int:pk>/', views.MedicamentoDeleteView.as_view(), name='eliminar_medicamento'),
]
