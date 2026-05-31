from django import forms
from django.utils import timezone
from inventario.models import Medicamento

class VentaForm(forms.Form):
    medicamento = forms.ModelChoiceField(
        queryset=Medicamento.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control',
            'placeholder': 'Selecciona un medicamento'
        }),
        label='Medicamento'
    )
    cantidad = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Cantidad',
            'min': '1'
        }),
        label='Cantidad'
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar solo medicamentos con stock disponible
        self.fields['medicamento'].queryset = Medicamento.objects.filter(stock__gt=0)
    
    def clean(self):
        cleaned_data = super().clean()
        medicamento = cleaned_data.get('medicamento')
        cantidad = cleaned_data.get('cantidad')
        
        if medicamento and cantidad:
            # Validar stock
            if cantidad > medicamento.stock:
                raise forms.ValidationError('No hay suficiente stock disponible')
            
            # Validar fecha de vencimiento
            fecha_hoy = timezone.now().date()
            if medicamento.fecha_vencimiento and medicamento.fecha_vencimiento < fecha_hoy:
                raise forms.ValidationError('Error: Este medicamento está vencido y no puede ser vendido.')
        
        return cleaned_data
    
    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
        medicamento = self.cleaned_data.get('medicamento')
        
        if medicamento and cantidad > medicamento.stock:
            raise forms.ValidationError(
                f'Error: Stock insuficiente. Cantidad disponible: {medicamento.stock}'
            )
        
        return cantidad
