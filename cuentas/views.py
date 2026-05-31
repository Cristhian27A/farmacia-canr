from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import RegistroForm

User = get_user_model()

class CustomLoginView(LoginView):
    template_name = 'cuentas/login.html'
    authentication_form = AuthenticationForm
    redirect_authenticated_user = True
    
    def form_valid(self, form):
        # El cambio está aquí: usamos 'form.get_user()' en lugar de 'self.get_user()'
        user = form.get_user() 
        
        if user and not user.is_active:
            messages.error(
                self.request,
                'Tu cuenta está desactivada. Contacta al administrador.'
            )
            return self.form_invalid(form)
            
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('core:home')

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('cuentas:login')

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, '¡Cuenta creada exitosamente!')
            return redirect('core:home')
    else:
        form = RegistroForm()
    
    return render(request, 'cuentas/registro.html', {'form': form})
