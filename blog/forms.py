from django import forms

class BlogPostForm(forms.Form):
    title = forms.CharField(label="Title", max_length=30)
    post = forms.CharField(label="Please write your post here", widget=forms.Textarea)