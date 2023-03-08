from django import forms
from .models import BlogPost
from django.forms import ModelForm, TextInput, Textarea

class BlogPostForm(ModelForm):  
    class Meta:
        model = BlogPost
        fields = ['title', 'post']
        widgets = {
            'title': TextInput(attrs={
                'class':'form-control',
                'style': 'max-width: 300px;',
                'placeholder':'Title'
            }),
            'post': Textarea(attrs={
                'class':'form-control',
                'placeholder':'Write your post here'
    
            })
        }


    # title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Title', 'style': 'width: 300px;', 'class': 'form-control'}))
    # post = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'New Post','class':'form-control'}))
    
    # title = forms.CharField(label="Title", max_length=30)
    # post = forms.CharField(label="Please write your post here", widget=forms.Textarea)