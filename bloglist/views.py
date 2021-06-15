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

"""
FUNZIONI DAL LIBRO DJANGO BY EXAMPLE (BLOG APPLICATION)

def post_list(request, tag_slug=None):    
    object_list = Post.published.all()
    tag = None
    

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    return render(request,
                  'blog/post/list.html',
                  {'posts': object_list, 'tag': tag})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})
"""
