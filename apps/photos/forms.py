from django import forms
from .models import Photo

class PhotoUploadForm(forms.ModelForm):
    """
    Formulário para upload de fotos.
    """
    class Meta:
        model = Photo
        fields = ['title', 'description', 'image']
        
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Pôr do sol na praia',
                'maxlength': '200'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Conte a história por trás da foto... (opcional)',
                'rows': 4
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/jpeg,image/png,image/jpg'
            })
        }
        
        labels = {
            'title': 'Título da Foto',
            'description': 'Descrição',
            'image': 'Selecione a Foto'
        }
        
        help_texts = {
            'title': 'Escolha um título chamativo para sua foto',
            'description': 'Opcional: Descreva o momento ou local',
            'image': 'Formatos: JPG, PNG | Tamanho máximo: 5MB'
        }
    
    def clean_image(self):
        """
        Validações customizadas para a imagem.
        """
        image = self.cleaned_data.get('image')
        
        if image:
            # Verificar tamanho (5MB máximo)
            if image.size > 5 * 1024 * 1024:  # 5MB em bytes
                raise forms.ValidationError(
                    'A imagem é muito grande! Tamanho máximo: 5MB'
                )
            
            # Verificar tipo de arquivo
            if not image.content_type in ['image/jpeg', 'image/png', 'image/jpg']:
                raise forms.ValidationError(
                    'Formato não suportado! Use apenas JPG ou PNG'
                )
        
        return image