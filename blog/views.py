from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, ListView, CreateView
from blog.forms import BlogPostForm
from blog.models import BlogPost

# Create your views here.

class HomeView(TemplateView):
    template_name = 'blog/home.html'



class BlogPostView(FormView):
    form_class = BlogPostForm
    template_name = 'blog/new_post.html'
    success_url = reverse_lazy('blog:posts')
    def form_valid(self, form):
        print(form.cleaned_data)
        form.save()
        return super().form_valid(form)

class Success(TemplateView):
    template_name = 'blog/success.html'

class Posts(ListView):
    model = BlogPost
    context_object_name = 'blog_posts'



