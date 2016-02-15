from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'my_blogs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'article.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/$', 'article.views.blog', name='blog'),
    url(r'^blog/(?P<article_id>\d+)/$', 'article.views.page', name='page')
)
