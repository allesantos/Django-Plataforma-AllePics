from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from .models import User


class UserRegisterForm(UserCreationForm):
    """
    Formulário de cadastro de usuário.
    """
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'seu@email.com'
        })
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'seu_usuario'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adicionar classes Bootstrap aos campos de senha
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': '••••••••'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': '••••••••'
        })
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este email já está cadastrado.')
        return email


class UserLoginForm(AuthenticationForm):
    """
    Formulário de login.
    """
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Seu usuário'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': '••••••••'
        })
    )

class ProfilePictureForm(forms.ModelForm):
    """Formulário para upload de foto de perfil"""
    
    class Meta:
        model = User
        fields = ['profile_picture']
        widgets = {
            'profile_picture': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/jpeg,image/jpg,image/png',
                'id': 'profilePictureInput',
            })
        }
        labels = {
            'profile_picture': '📸 Foto de Perfil'
        }
    
    def clean_profile_picture(self):
        """Valida tamanho da imagem"""
        picture = self.cleaned_data.get('profile_picture')
        
        if picture:
            # Verificar tamanho (máx 2MB)
            if picture.size > 2 * 1024 * 1024:
                raise ValidationError('A foto deve ter no máximo 2MB.')
            
            # Verificar tipo
            if not picture.content_type in ['image/jpeg', 'image/jpg', 'image/png']:
                raise ValidationError('Apenas arquivos JPG, JPEG ou PNG são permitidos.')
        
        return picture
    
class UserEditForm(forms.ModelForm):
    """Formulário para editar dados pessoais do usuário"""
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite seu nome',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite seu sobrenome',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'seu@email.com',
            }),
        }
        labels = {
            'first_name': '👤 Nome',
            'last_name': '👤 Sobrenome',
            'email': '📧 Email',
        }
    
    def __init__(self, *args, **kwargs):
        """Personaliza o formulário ao inicializar"""
        super().__init__(*args, **kwargs)
        # Tornar campos opcionais
        self.fields['first_name'].required = False
        self.fields['last_name'].required = False
        # Email é obrigatório
        self.fields['email'].required = True
    
    def clean_email(self):
        """Valida email único (exceto do próprio usuário)"""
        email = self.cleaned_data.get('email')
        user_id = self.instance.id
        
        # Verificar se email já existe (ignorando o próprio usuário)
        if User.objects.exclude(id=user_id).filter(email=email).exists():
            raise ValidationError('Este email já está sendo usado por outro usuário.')
        
        return email