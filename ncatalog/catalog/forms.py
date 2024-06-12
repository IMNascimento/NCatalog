from django import forms
from .models import Clothing, Comment

class ClothingForm(forms.ModelForm):
    class Meta:
        model = Clothing
        fields = ['title', 'path', 'description']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']