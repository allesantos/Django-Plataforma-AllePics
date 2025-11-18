from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),  # Página inicial
    path('', include('apps.users.urls')),  # URLs de usuários
    path('', include('apps.photos.urls')),
]

# Servir arquivos MEDIA em desenvolvimento
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )