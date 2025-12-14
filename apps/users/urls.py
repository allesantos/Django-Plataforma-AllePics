from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('cadastro/', views.register_view, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('perfil/', views.profile_view, name='profile'),
    path('perfil/editar-foto/', views.edit_profile_picture_view, name='edit_profile_picture'),
    path('perfil/editar/', views.edit_profile_view, name='edit_profile'), 
    path('perfil/remover-foto/', views.remove_profile_picture_view, name='remove_profile_picture'),  
]