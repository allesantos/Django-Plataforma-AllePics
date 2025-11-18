from django.db import models
from django.conf import settings
from django.utils import timezone

class Photo(models.Model):
    """
    Model para armazenar fotos dos usuários.
    """
    # Relacionamento: Cada foto pertence a um usuário
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='photos',
        verbose_name='Usuário'
    )
    
    # Informações da foto
    title = models.CharField(
        'Título',
        max_length=200,
        help_text='Dê um título para sua foto'
    )
    
    description = models.TextField(
        'Descrição',
        blank=True,
        null=True,
        help_text='Descreva sua foto (opcional)'
    )
    
    # Arquivo da imagem
    image = models.ImageField(
        'Imagem',
        upload_to='photos/%Y/%m/%d/',
        help_text='Formatos aceitos: JPG, PNG'
    )
    
    # Datas
    uploaded_at = models.DateTimeField(
        'Data de Upload',
        default=timezone.now
    )
    
    updated_at = models.DateTimeField(
        'Última Atualização',
        auto_now=True
    )
    
    class Meta:
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos'
        ordering = ['-uploaded_at']  # Mais recentes primeiro
    
    def __str__(self):
        return f'{self.title} - {self.user.username}'
    
    def delete(self, *args, **kwargs):
        """
        Sobrescreve o método delete para apagar o arquivo físico também.
        """
        # Apagar arquivo físico
        if self.image:
            self.image.delete(save=False)
        
        # Apagar do banco de dados
        super().delete(*args, **kwargs)