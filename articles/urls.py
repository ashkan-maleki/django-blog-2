__author__ = 'Johnny Cage'

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.ArticleStreamView.as_view(), name='index'),
    url(r'^articles/$', views.ArticleListView.as_view(), name='list'),
    url(r'^create/$', views.ArticleCreate.as_view(), name='create'),
    url(r'^tags/$', views.TagCreate.as_view(), name='tags'),
    url(r'^tags/(?P<year>[0-9]{4})/articles/$', views.ArticleByYearListView.as_view(), name='articles_by_year'),
    url(r'^tags/(?P<title>[ \w]+)/articles/$', views.ArticleByTagListView.as_view(), name='articles_by_tag'),
    url(r'^tags/(?P<pk>[0-9]+)/delete/$', views.TagDeleteView.as_view(), name='tag_delete'),
    url(r'^(?P<slug>[-\w]+)/update/$', views.ArticleUpdate.as_view(), name='update'),
    url(r'^(?P<slug>[-\w]+)/delete/$', views.ArticleDelete.as_view(), name='delete'),
    url(r'^(?P<slug>[-\w]+)/$', views.ArticleDetailView.as_view(), name='detail'),
]
