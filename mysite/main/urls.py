from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)

from . import views
from users import views as user_views

urlpatterns = [
    path('', PostListView.as_view(), name="main-home"),
    path('user/<str:username>', UserPostListView.as_view(), name="user-posts"),
    path('about/', views.about, name="main-about"),
    path('home/', PostListView.as_view(), name="main-home"),
    path('register/', user_views.register, name="register"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/new/', PostCreateView.as_view(), name="post-create"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),
    
]