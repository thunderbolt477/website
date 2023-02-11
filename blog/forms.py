from django.forms import ModelForm, Textarea
from .models import BlogPost

class BlogPostForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'post')
        widgets = {
            'post':Textarea(attrs={'cols':80, 'rows':20})
        }

    # title = forms.CharField(label="Title", max_length=30)
    # post = forms.CharField(label="Please write your post here", widget=forms.Textarea)