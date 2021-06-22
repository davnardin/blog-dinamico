from django.shortcuts import render, get_object_or_404
from .models import Post 
from django.views.generic import DetailView

def home(request):
    return render(request, 'blog/index.html')

class Dettaglio(DetailView):
    model = Post
    template_name = "blog/dettaglio.html"
    

def prova(request):
    object_list = Post.objects.filter(categoria__descrizione='google-ads')
    return render(request, 'blog/prova.html', {'posts': object_list})


