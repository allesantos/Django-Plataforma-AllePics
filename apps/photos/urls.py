from django.urls import path
from . import views

app_name = 'photos'

urlpatterns = [
    path('upload/', views.upload_photo_view, name='upload'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('photo/<int:photo_id>/', views.photo_detail_view, name='detail'),
    path('photo/<int:photo_id>/delete/', views.photo_delete_view, name='delete'),
]