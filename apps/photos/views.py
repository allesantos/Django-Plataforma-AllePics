from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .forms import PhotoUploadForm, PhotoSearchForm 
from .models import Photo
import os

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
    Galeria de fotos com busca e filtros.
    Usa select_related para reduzir queries ao banco.
    """
    # Pegar apenas as fotos do usuário logado (otimizado)
    photos = Photo.objects.filter(user=request.user).select_related('user')
    
    # Criar instância do formulário com os dados GET
    form = PhotoSearchForm(request.GET)
    
    # Aplicar busca se houver
    search_query = request.GET.get('search', '').strip()
    if search_query:
        photos = photos.filter(title__icontains=search_query)
    
    # Aplicar ordenação se houver
    order_by = request.GET.get('order', '-uploaded_at')
    if order_by:
        photos = photos.order_by(order_by)
    
    # Paginação (12 fotos por página)
    paginator = Paginator(photos, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Calcular informações da paginação
    start_index = (page_obj.number - 1) * paginator.per_page + 1
    end_index = min(page_obj.number * paginator.per_page, paginator.count)
    
    context = {
        'photos': page_obj.object_list,
        'page_obj': page_obj,          
        'total_photos': photos.count(), 
        'form': form,                   
        'search_query': search_query,   
        'start_index': start_index,    
        'end_index': end_index,        
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