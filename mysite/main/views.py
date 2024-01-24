from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
# Create your views here.


def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request,'main/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'main/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted'] # date_posted jeśli chcemy od najstarszego
    # <app>/<model>_<viewtype>.html - wyświetlanie błędu

class PostDetailView(DetailView):
    model = Post
    
    
def about(request):
    return render(request,'main/about.html', {'title': 'About'})
