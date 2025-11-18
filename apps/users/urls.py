from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('cadastro/', views.register_view, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('perfil/', views.profile_view, name='profile'),
]