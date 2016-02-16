from django.shortcuts import render
from django.http import HttpResponse, Http404
from datetime import datetime
from .models import Article
# Create your views here.

def home(request):
    return render(request, 'home.html')


def blog(request):
    post_list = Article.objects.all()
    return render(request, 'blog.html', {'post_list': post_list})

def page(request, article_id):
    try:
        post = Article.objects.get(id=str(article_id))
    except Article.DoesNotExist:
        raise Http404('Article does not exists')
    return render(request, 'page.html', {'post': post})

def search_tag(request,tag):
    try:
        post_list = Article.objects.filter(category__iexact = tag)
    except Aritcle.DoesNotExist:
        raise Http404
    return render(request, 'tag.html', {'post_list': post_list})

def aboutme(request):
    return render(request, 'aboutme.html')
