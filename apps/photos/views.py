from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PhotoUploadForm

@login_required
def upload_photo_view(request):
    """
    View para fazer upload de fotos.
    Apenas usuários logados podem acessar.
    """
    if request.method == 'POST':
        form = PhotoUploadForm(request.POST, request.FILES)
        
        if form.is_valid():
            # Criar foto mas não salvar ainda
            photo = form.save(commit=False)
            
            # Associar ao usuário logado
            photo.user = request.user
            
            # Agora sim salvar
            photo.save()
            
            messages.success(
                request,
                f'Foto "{photo.title}" enviada com sucesso! 📸✨'
            )
            
            return redirect('photos:upload')
        else:
            messages.error(
                request,
                'Erro ao enviar foto. Verifique os campos.'
            )
    else:
        form = PhotoUploadForm()
    
    context = {
        'form': form
    }
    
    return render(request, 'photos/upload.html', context)