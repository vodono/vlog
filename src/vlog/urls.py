from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns
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
        "^categories/(?P<category_slug>[\w'-]+)/$",
        views.CategoryView.as_view(),
        name='category'
    ),
    re_path(
        '^articles/$',
        views.ArticlesView.as_view(),
        name='articles'
    ),
    re_path(
        "^articles/(?P<article_slug>[\w'-]+)/$",
        views.ArticleView.as_view(),
        name='article'
    ),
    re_path(
        '^tags/$',
        views.TagsView.as_view(),
        name='tags'
    ),
    re_path(
        "^tags/(?P<tag_slug>[\w'-]+)/$",
        views.TagView.as_view(),
        name='tag'
    ),
    re_path(
        '^api/v1/categories/$',
        views.CategoriesList.as_view()
    ),
    re_path(
        "^api/v1/categories/(?P<category_slug>[\w'-]+)/$",
        views.CategoryDetail.as_view()
    ),
    re_path(
        '^api/v1/articles/$',
        views.ArticlesList.as_view()
    ),
    re_path(
        "^api/v1/articles/(?P<article_slug>[\w'-]+)/$",
        views.ArticleDetail.as_view()
    ),
    re_path(
        '^api/v1/tags/$',
        views.TagsList.as_view()
    ),
    re_path(
        "^api/v1/categories/(?P<article_slug>[\w'-]+)/$",
        views.ArticleDetail.as_view()
    ),
    re_path(
        "^api/v1/tags/(?P<tag_slug>[\w'-]+)/$",
        views.TagDetail.as_view()
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
