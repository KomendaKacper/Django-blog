from django.urls import path
from . import views
from users import views as user_views

urlpatterns = [
    path('', views.home, name="main-home"),
    path('about/', views.about, name="main-about"),
    path('home/', views.home, name="main-home"),
    path('register/', user_views.register, name="register"),
]