from django.urls import path
from .views import PostListView, PostDetailView
from . import views
from users import views as user_views

urlpatterns = [
    path('', views.home, name="main-home"),
    path('about/', views.about, name="main-about"),
    path('home/', PostListView.as_view(), name="main-home"),
    path('register/', user_views.register, name="register"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),

]