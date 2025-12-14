from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import FileExtensionValidator


class User(AbstractUser):
    """
    User Model customizado para o AllePics.
    
    Herda de AbstractUser que já tem:
    - username, email, password
    - first_name, last_name
    - is_active, is_staff, date_joined
    """
    
    profile_picture = models.ImageField(
        upload_to='profile_pictures/%Y/%m/%d/',
        null=True,
        blank=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=['jpg', 'jpeg', 'png'],
                message='Apenas arquivos JPG, JPEG ou PNG são permitidos.'
            )
        ],
        help_text='Foto de perfil (JPG, JPEG ou PNG, máx 2MB)'
    )
    
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['-date_joined']
    
    def __str__(self):
        return self.username
    
    @property
    def has_profile_picture(self):
        """Verifica se o usuário tem foto de perfil"""
        return bool(self.profile_picture)