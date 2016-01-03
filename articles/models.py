from autoslug import AutoSlugField
from django.db import models
from django.utils import timezone


class Tag(models.Model):
    title = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.title


class Article(models.Model):
    tags = models.ManyToManyField(Tag, null=False, blank=False)
    title = models.CharField(max_length=120)
    slug = AutoSlugField(populate_from='title', unique=True)
    content = models.TextField()
    published_date = models.DateTimeField('date published', default=timezone.now())
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-published_date']
