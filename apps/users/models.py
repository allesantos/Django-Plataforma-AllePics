from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    User Model customizado para o AllePics.
    
    Herda de AbstractUser que já tem:
    - username
    - email
    - password
    - first_name
    - last_name
    - is_active
    - is_staff
    - date_joined
    """
    
    # Por enquanto, só herda do AbstractUser
    # Depois vamos adicionar: bio, avatar, etc.
    
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['-date_joined']  # Mais recentes primeiro
    
    def __str__(self):
        return self.username