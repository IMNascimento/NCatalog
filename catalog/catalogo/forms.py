from django import forms
from .models import Photography
from django.forms import ModelForm


class PhotographyForm(forms.ModelForm):
    class Meta:
        model = Photography
        fields = "__all__"
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
    

class LoginForms(forms.Form):
    email=forms.CharField(
        label='Nome de Login', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: João Silva',
            }
        )
    )
    senha=forms.CharField(
        label='Senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha',
            }
        ),
    )

class CadastroForms(forms.Form):
    nome_cadastro=forms.CharField(
        label='Nome de Cadastro', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: João Silva',
            }
        )
    )
    email=forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: joaosilva@xpto.com',
            }
        )
    )
    senha_1=forms.CharField(
        label='Senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha',
            }
        ),
    )
    senha_2=forms.CharField(
        label='Confirme a sua senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha novamente',
            }
        ),
    )

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')

        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('Espaços não são permitidos nesse campo')
            else:
                return nome

    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get('senha_1')
        senha_2 = self.cleaned_data.get('senha_2')

        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError('Senhas não são iguais')
            else:
                return senha_2