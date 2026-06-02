from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Medicamento, Categoria
from .forms import MedicamentoForm

@login_required
def index(request):
    return render(request, 'inventario/index.html')

class MedicamentoListView(LoginRequiredMixin, ListView):
    model = Medicamento
    template_name = 'inventario/lista_medicamentos.html'
    context_object_name = 'medicamentos'
    ordering = ['-fecha_registro']
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        categoria_id = self.request.GET.get('categoria')
        
        if query:
            queryset = queryset.filter(
                nombre__icontains=query
            ) | queryset.filter(
                descripcion__icontains=query
            )
        
        if categoria_id:
            queryset = queryset.filter(categoria_id=categoria_id)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        context['categoria_seleccionada'] = self.request.GET.get('categoria', '')
        return context

class MedicamentoCreateView(LoginRequiredMixin, CreateView):
    model = Medicamento
    form_class = MedicamentoForm
    template_name = 'inventario/medicamento_form.html'
    success_url = reverse_lazy('inventario:lista_medicamentos')

class MedicamentoUpdateView(LoginRequiredMixin, UpdateView):
    model = Medicamento
    form_class = MedicamentoForm
    template_name = 'inventario/medicamento_form.html'
    success_url = reverse_lazy('inventario:lista_medicamentos')

class MedicamentoDeleteView(LoginRequiredMixin, DeleteView):
    model = Medicamento
    template_name = 'inventario/medicamento_confirm_delete.html'
    success_url = reverse_lazy('inventario:lista_medicamentos')
