from django.urls import path
from .views import HomeView, NewPostView, Success, Posts

app_name = 'blog'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('new_post/',NewPostView.as_view(), name='new_post'),
    path('success/', Success.as_view(), name='success'),
    path('posts/', Posts.as_view(), name='posts')
]