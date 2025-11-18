from django.contrib import admin
from .models import Photo

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    """
    Admin customizado para o Model Photo.
    """
    list_display = [
        'title',
        'user',
        'uploaded_at',
        'image_preview'
    ]
    
    list_filter = [
        'uploaded_at',
        'user'
    ]
    
    search_fields = [
        'title',
        'description',
        'user__username'
    ]
    
    readonly_fields = [
        'uploaded_at',
        'updated_at',
        'image_preview'
    ]
    
    ordering = ['-uploaded_at']
    
    def image_preview(self, obj):
        """
        Mostra preview da imagem no admin.
        """
        if obj.image:
            return f'<img src="{obj.image.url}" width="100" height="100" style="object-fit: cover;" />'
        return 'Sem imagem'
    
    image_preview.short_description = 'Preview'
    image_preview.allow_tags = True