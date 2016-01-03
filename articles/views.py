from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.views.generic import edit, View, TemplateView
from django.views.generic.edit import FormMixin
from django.views.generic.list import ListView, MultipleObjectMixin
from django.views.generic.detail import DetailView, SingleObjectMixin
from articles.forms import ArticleForm, TagForm
from articles.models import Article, Tag
from django.db.models import F


class ArticleModel(SingleObjectMixin):
    model = Article


class ArticleModelForm(FormMixin):
    form_class = ArticleForm
    success_url = reverse_lazy('articles:list')


class ArticleListView(ListView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['articles'] = Article.objects.all()
        return context


class ArticleDetailView(DetailView, ArticleModel):
    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['article'] = get_object_or_404(Article, slug=self.kwargs.get('slug', None))
        return context


class ArticleCreate(edit.CreateView, ArticleModel, ArticleModelForm):
    template_name_suffix = '_create'


class ArticleUpdate(edit.UpdateView, ArticleModel, ArticleModelForm):
    template_name_suffix = '_update'


class ArticleDelete(edit.DeleteView, ArticleModel):
    success_url = reverse_lazy('articles:list')


class ArticleStreamView(ArticleListView):
    template_name_suffix = '_stream'

    def get_context_data(self, **kwargs):
        context = super(ArticleStreamView, self).get_context_data(**kwargs)
        context['articles'] = Article.objects.all()

        dates = Article.objects.values('published_date').order_by('-published_date')
        years = {}
        for date in dates:
            year = date['published_date'].strftime('%Y')
            years[year] = year
        self.request.session['articles_by_year'] = years

        tag_objects = Tag.objects.all()
        tags = {}
        for tag_obj in tag_objects:
            tag = str(tag_obj)
            tags[tag] = tag
        self.request.session['tags'] = tags

        return context


class ArticleByTagListView(ArticleStreamView):
    def get_context_data(self, **kwargs):
        context = super(ArticleByTagListView, self).get_context_data(**kwargs)
        tag = get_object_or_404(Tag, title=self.kwargs.get('title', None))
        context['articles'] = tag.article_set.all()
        return context


class ArticleByYearListView(ArticleStreamView):
    def get_context_data(self, **kwargs):
        context = super(ArticleByYearListView, self).get_context_data(**kwargs)
        context['articles'] = get_list_or_404(Article, published_date__year=self.kwargs.get('year', None))
        return context


class TagCreate(edit.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy('articles:create')

    def get_context_data(self, **kwargs):
        context = super(TagCreate, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context


class TagDeleteView(edit.DeleteView):
    model = Tag
    success_url = reverse_lazy('articles:tags')
