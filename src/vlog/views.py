from core.views import BaseView
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from vlog.models import Category, Article, Tag
from django.db.models import Count


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

