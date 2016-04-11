from django import forms
from .models import *

class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
    attrs={
        'class': 'form-control input-lg',
        'placeholder': 'Title'
        }
    ))
    text = forms.CharField(widget=forms.Textarea(
    attrs={
        'class': 'form-control',
        'placeholder': 'Text'
        }
    ))

    class Meta:
        model =  Post
        fields = ['title', 'text', 'image', 'user']
