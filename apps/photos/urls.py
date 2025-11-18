from django.urls import path
from . import views

app_name = 'photos'

urlpatterns = [
    path('upload/', views.upload_photo_view, name='upload'),
]