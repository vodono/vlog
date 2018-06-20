from django.urls import path, re_path

from vlog import views

urlpatterns = [
    re_path('^$', views.IndexView.as_view(), name='index'),
    re_path('^index$', views.IndexView.as_view(), name='index'),
    re_path('^index/$', views.IndexView.as_view(), name='index'),
    re_path(
        '^categories/$',
        views.CategoriesView.as_view(),
        name='categories'
    ),
    re_path(
        '^categories/(?P<category_slug>[\w-]+)/$',
        views.CategoryView.as_view(),
        name='category'
    ),
    re_path(
        '^articles/$',
        views.ArticlesView.as_view(),
        name='articles'
    ),
    re_path(
        '^articles/(?P<article_slug>[\w-]+)/$',
        views.ArticleView.as_view(),
        name='article'
    ),
    re_path(
        '^tags/$',
        views.TagsView.as_view(),
        name='tags'
    ),
    re_path(
        '^tags/(?P<tag_slug>[\w-]+)/$',
        views.TagView.as_view(),
        name='tag'
    ),
]
