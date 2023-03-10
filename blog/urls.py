from django.urls import path
from .views import HomeView, BlogPostView, Success, Posts, SinglePost

app_name = 'blog'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('new_post/',BlogPostView.as_view(), name='blog_post'),
    path('success/', Success.as_view(), name='success'),
    path('posts/', Posts.as_view(), name='posts'),
    path("posts/<int:pk>",SinglePost.as_view(), name='post_detail_view')
]