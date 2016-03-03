from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from datetime import datetime
from .models import Article, Tag
# Create your views here.

def home(request):
    return render(request, 'home.html')


def blog(request):
    posts = Article.objects.all()
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    page_range = paginator.page_range
    tag_list = Tag.objects.all()
    try :
        post_list = paginator.page(page)
    except PageNotAnInteger :
        post_list = paginator.page(1)
    except EmptyPage :
        post_list = paginator.paginator(paginator.num_pages)
    return render(request, 'blog.html', {'post_list': post_list,
                                         'page_range': page_range,
                                         'tag_list': tag_list})

def page(request, article_id):
    try:
        post = Article.objects.get(id=str(article_id))
        tag_list = Tag.objects.all()
    except Article.DoesNotExist:
        raise Http404('Article does not exists')
    return render(request, 'page.html', {'post': post,
                                         'tag_list': tag_list})

def search_tag(request,tag):
    try:
        tag_list = Tag.objects.all()
        this_category = Tag.objects.get(category = tag)
        post_list = this_category.article_set.all()
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'tag.html', {'post_list': post_list,
                                        'tag_list': tag_list})

def aboutme(request):
    return render(request, 'aboutme.html')
