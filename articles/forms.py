__author__ = 'Johnny Cage'
from django import forms
from .models import Article, Tag


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['timestamp', 'slug']
        fields = ['title', 'content', 'published_date', 'tags']


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['title']
