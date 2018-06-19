from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _

from ckeditor.fields import RichTextField

from core.models import BaseModel


class Publication(BaseModel):
    title = models.CharField(
        max_length=100,
        unique=True,
        verbose_name=_('Title')
    )

    slug = models.CharField(
        max_length=150,
        unique=True,
        blank=True,
        verbose_name=_('Slug'),
        help_text="Don't change the field manually!"
    )

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class Category(Publication):
    image = models.ImageField(
        null=True,
        blank=True
    )

    description = models.CharField(
        max_length=200,
        verbose_name=_('Description'),
        null=True
    )

    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        related_name='categories',
        verbose_name=_('Author'),
        on_delete=models.SET_NULL,
        null=True
    )

    class Meta:
        db_table = 'category'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Article(Publication):
    description = models.CharField(
        max_length=200,
        verbose_name=_('Description'),
        null=True
    )

    content = RichTextField()

    image = models.ImageField(
        null=True,
        blank=True
    )

    publication_date = models.DateField(
        verbose_name = _('Publicated'),
        auto_now = False,
        null = True,
        blank = True
    )

    visible = models.BooleanField(
        default=False
    )

    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        related_name='articles',
        verbose_name=_('Author'),
        on_delete=models.SET_NULL,
        null=True
    )

    category = models.ForeignKey(
        to='Category',
        related_name='articles',
        verbose_name=_('Category'),
        on_delete=models.SET_NULL,
        null=True
    )

    class Meta:
        db_table = 'article'
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')


class Tag(Publication):
    articles = models.ManyToManyField(
        to='Article',
        related_name='tags',
        verbose_name=_('Articles'),
        db_table='tag__article'
    )

    class Meta:
        db_table = 'tag'
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')


class Comment(BaseModel):
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        related_name='comments',
        verbose_name=_('Author'),
        on_delete=models.SET_NULL,
        null=True
    )

    article = models.ForeignKey(
        to='Article',
        related_name='comments',
        verbose_name=_('Article'),
        on_delete=models.CASCADE
    )

    text = models.TextField(
        verbose_name=_('Text')
    )

    def __str__(self):
        return f'{self.author.username} [{self.article.title}]'

    class Meta:
        db_table = 'comment'
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')
