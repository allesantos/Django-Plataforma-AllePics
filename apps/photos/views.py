from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .forms import PhotoUploadForm
from .models import Photo

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

@login_required
def gallery_view(request):
    """
    View para exibir galeria de fotos do usuário.
    Com paginação de 12 fotos por página.
    """
    # Buscar apenas fotos do usuário logado
    photos_list = Photo.objects.filter(user=request.user)
    
    # Configurar paginação
    paginator = Paginator(photos_list, 12)  # 12 fotos por página
    page_number = request.GET.get('page')
    photos = paginator.get_page(page_number)
    
    context = {
        'photos': photos,
        'total_photos': photos_list.count()
    }
    
    return render(request, 'photos/gallery.html', context)


@login_required
def photo_detail_view(request, photo_id):
    """
    View para exibir detalhes de uma foto.
    Apenas o dono pode ver.
    """
    # Buscar foto e garantir que pertence ao usuário
    photo = get_object_or_404(Photo, id=photo_id, user=request.user)
    
    context = {
        'photo': photo
    }
    
    return render(request, 'photos/detail.html', context)


@login_required
def photo_delete_view(request, photo_id):
    """
    View para deletar uma foto.
    Apenas o dono pode deletar.
    """
    # Buscar foto e garantir que pertence ao usuário
    photo = get_object_or_404(Photo, id=photo_id, user=request.user)
    
    if request.method == 'POST':
        photo_title = photo.title
        
        # Deletar foto (método delete customizado apaga arquivo também)
        photo.delete()
        
        messages.success(
            request,
            f'Foto "{photo_title}" deletada com sucesso! 🗑️'
        )
        
        return redirect('photos:gallery')
    
    # Se não for POST, redireciona para galeria
    return redirect('photos:gallery')