from django import forms
from .models import Photography
from django.forms import ModelForm


class PhotographyForm(forms.ModelForm):
    class Meta:
        model = Photography
        fields = "__all__"
        exclude= ["like"]
        labels = {
            'name': "Nome:",
            'subtitle': "Subtitulo:",
            'category': "Categoria:",
            'user': "Usuário:",
            'published': "Deseja Publicar ?",
            'date_photography': "Data da imagem:",
            'path': "Faça upload:",
            'description': "Descrição:",          
            }
        widgets = {
            'name': forms.TextInput(
                attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: João Silva',
            }),
            'subtitle': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ex.: João Silva',
            }),
            'user': forms.Select(
                attrs={
                    'class': 'form-select',
            }),
            'category': forms.Select(
                attrs={
                    'class': 'form-select',
            }),
            'description': forms.Textarea(
                attrs={
                'class': 'form-control',
                'placeholder': 'Descreva sobre a imagem',
            }),
            'date_photography': forms.DateInput(
                attrs={
                'class': 'form-control',
                'input_formats': '%m/%d/%Y',
            }),
            'path': forms.ClearableFileInput(
                attrs={
                'class': 'form-control',
            }),
            
        }


class PhotographyDisplayForm(forms.ModelForm):
    class Meta:
        model = Photography
        fields = ['name','subtitle','user','category','description','date_photography']
        labels = {
            'name': "Nome:",
            'subtitle': "Subtitulo:",
            'category': "Categoria:",
            'user': "Usuário:",
            'date_photography': "Data da imagem:",
            'description': "Descrição:",          
            }
        widgets = {
            'name': forms.TextInput(
                attrs={
                'class': 'form-control',
                'disabled': 'disabled'
            }),
            'subtitle': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'disabled': 'disabled'
            }),
            'user': forms.Select(
                attrs={
                    'class': 'form-select',
                    'disabled': 'disabled'
            }),
            'category': forms.Select(
                attrs={
                    'class': 'form-select',
                    'disabled': 'disabled'
            }),
            'description': forms.Textarea(
                attrs={
                'class': 'form-control',
                'disabled': 'disabled',
            }),
            'date_photography': forms.DateInput(
                attrs={
                'class': 'form-control',
                'input_formats': '%m/%d/%Y',
                'disabled': 'disabled'
            }),
            'path': forms.ClearableFileInput(
                attrs={
                'class': 'form-control',
                'disabled': 'disabled'
            }),
            
        }
    


