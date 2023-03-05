from django import forms
from .models import BlogPost

class BlogPostForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 300px;', 'class': 'form-control'}))
    post = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'New Post','class':'form-control'}))
    
    
    # class Meta:
    #     model = BlogPost
    #     fields = ('title', 'post')
    #     widgets = {
    #         'post':Textarea(attrs={'cols':80, 'rows':20},{class=''})
    #     }

    # title = forms.CharField(label="Title", max_length=30)
    # post = forms.CharField(label="Please write your post here", widget=forms.Textarea)