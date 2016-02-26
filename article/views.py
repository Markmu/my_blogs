from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from datetime import datetime
from .models import Article
# Create your views here.

def home(request):
    return render(request, 'home.html')


def blog(request):
    posts = Article.objects.all()
    paginator = Paginator(posts, 8)
    page = request.GET.get('page')
    page_range = paginator.page_range
    try :
        post_list = paginator.page(page)
    except PageNotAnInteger :
        post_list = paginator.page(1)
    except EmptyPage :
        post_list = paginator.paginator(paginator.num_pages)
    return render(request, 'blog.html', {'post_list': post_list,
                                         'page_range': page_range})

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
