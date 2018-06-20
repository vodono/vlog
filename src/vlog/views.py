from core.views import BaseView
from vlog.models import Category, Article, Tag
from django.db.models import Count
from django.shortcuts import render_to_response
from django.views.generic import TemplateView


class IndexView(BaseView):
    template_name = 'vlog/index.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        categories = Category.objects \
                         .annotate(category_population=Count('articles')) \
                         .order_by('-category_population')[:3]
        context.update({'categories': categories})

        articles = Article.objects \
                       .annotate(article_comments=Count('comments')) \
                       .order_by('-article_comments')[:10]
        context.update({'articles': articles})

        tags = Tag.objects \
                   .annotate(tags_articles=Count('articles')) \
                   .order_by('-tags_articles')[:10]
        context.update({'tags': tags})

        return self.render_to_response(context)


class CategoriesView(BaseView):
    template_name = 'vlog/categories.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        categories = Category.objects \
                        .all() \
                        .annotate(category_articles=Count('articles')) \
                        .order_by('-category_articles')
        context.update({'categories': categories})

        return self.render_to_response(context)

class CategoryView(BaseView):
    template_name = 'vlog/category.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        category = Category.objects.get(slug=kwargs.get('category_slug'))
        context.update({'category': category})

        top_articles = Article.objects \
            .filter(category__slug=kwargs.get('category_slug')) \
            .annotate(articles_comments=Count('comments')) \
            .order_by('-articles_comments')
        context.update({'top_articles': top_articles})

        return self.render_to_response(context)

class ArticlesView(BaseView):
    template_name = 'vlog/articles.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        articles = Article.objects.all()\
            .annotate(comments_qty=Count('comments'))\
            .order_by('-comments_qty')

        context.update({'articles': articles})

        return self.render_to_response(context)

class ArticleView(BaseView):
    template_name = 'vlog/article.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        article = Article.objects.get(slug=kwargs.get('article_slug'))
        context.update({'article': article})

        return self.render_to_response(context)

class TagsView(BaseView):
    template_name = 'vlog/tags.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        tags = Tag.objects.all()\
            .annotate(articles_qty=Count('articles'))\
            .order_by('-articles_qty')
        context.update({'tags': tags})

        articles_by_tag = Article.objects.values('tags', 'title', 'slug')\
            .annotate(comments_qty=Count('comments'))\
            .order_by('tags', '-comments_qty')
        context.update({'articles_by_tag': articles_by_tag})


        return self.render_to_response(context)

class TagView(BaseView):
    template_name = 'vlog/tag.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        tag = Tag.objects.get(slug=kwargs.get('tag_slug'))
        context.update({'tag': tag})

        articles = Article.objects \
            .filter(tags__slug=kwargs.get('tag_slug')) \
            .annotate(articles_comments=Count('comments')) \
            .order_by('-articles_comments')
        context.update({'articles': articles})

        return self.render_to_response(context)
