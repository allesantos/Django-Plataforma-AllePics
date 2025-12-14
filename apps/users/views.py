from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import UserRegisterForm, UserLoginForm, ProfilePictureForm, UserEditForm
import os

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


@login_required
def edit_profile_picture_view(request):
    """
    View para editar foto de perfil do usuário.
    """
    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES, instance=request.user)
        
        if form.is_valid():
            # Apagar foto antiga se existir
            old_picture = request.user.profile_picture
            
            # Salvar nova foto
            user = form.save()
            
            # Apagar arquivo físico da foto antiga
            if old_picture and old_picture != user.profile_picture:
                if os.path.isfile(old_picture.path):
                    os.remove(old_picture.path)
            
            messages.success(request, '✅ Foto de perfil atualizada com sucesso!')
            return redirect('users:profile')
        else:
            messages.error(request, '❌ Erro ao atualizar foto. Verifique o arquivo.')
    else:
        form = ProfilePictureForm(instance=request.user)
    
    context = {
        'form': form
    }
    return render(request, 'users/edit_profile_picture.html', context)


@login_required
def edit_profile_view(request):
    """
    View para editar dados pessoais do usuário.
    """
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Informações atualizadas com sucesso!')
            return redirect('users:profile')
        else:
            messages.error(request, '❌ Erro ao atualizar informações. Verifique os dados.')
    else:
        form = UserEditForm(instance=request.user)
    
    context = {
        'form': form
    }
    return render(request, 'users/edit_profile.html', context)

@login_required
def remove_profile_picture_view(request):
    """
    View para remover foto de perfil.
    """
    if request.method == 'POST':
        user = request.user
        
        # Verificar se usuário tem foto
        if user.profile_picture:
            # Guardar caminho antes de deletar
            photo_path = user.profile_picture.path
            
            # Remover do banco
            user.profile_picture.delete(save=True)
            
            # Remover arquivo físico
            if os.path.isfile(photo_path):
                os.remove(photo_path)
            
            messages.success(request, '✅ Foto de perfil removida com sucesso!')
        else:
            messages.info(request, 'ℹ️ Você não possui foto de perfil.')
        
        return redirect('users:profile')
    
    # Se não for POST, redireciona para perfil
    return redirect('users:profile')