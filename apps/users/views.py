from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import UserRegisterForm, UserLoginForm


def register_view(request):
    """
    View de cadastro de usuário.
    """
    if request.user.is_authenticated:
        # Se já está logado, redireciona para home
        return redirect('core:home')
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Salvar usuário
            user = form.save()
            username = form.cleaned_data.get('username')
            
            # Fazer login automático
            login(request, user)
            
            # Mensagem de sucesso
            messages.success(request, f'Bem-vindo ao AllePics, {username}! 🎉')
            return redirect('core:home')
        else:
            # Mensagem de erro
            messages.error(request, 'Corrija os erros abaixo.')
    else:
        form = UserRegisterForm()
    
    return render(request, 'users/register.html', {'form': form})


class CustomLoginView(LoginView):
    """
    View de login customizada.
    """
    template_name = 'users/login.html'
    form_class = UserLoginForm
    redirect_authenticated_user = True
    
    def form_valid(self, form):
        """Executado quando o login é bem-sucedido."""
        messages.success(self.request, f'Bem-vindo de volta, {form.get_user().username}! 👋')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """Executado quando o login falha."""
        messages.error(self.request, 'Usuário ou senha incorretos.')
        return super().form_invalid(form)


def logout_view(request):
    """
    View de logout.
    """
    username = request.user.username if request.user.is_authenticated else None
    logout(request)
    if username:
        messages.info(request, f'Até logo, {username}! 👋')
    return redirect('core:home')


@login_required
def profile_view(request):
    """
    View para exibir perfil do usuário.
    """
    # Contar fotos do usuário
    total_photos = request.user.photos.count()
    
    context = {
        'total_photos': total_photos
    }
    
    return render(request, 'users/profile.html', context)