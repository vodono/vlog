from django.urls import path, re_path

from vlog import views

urlpatterns = [
    re_path('^$', views.IndexView.as_view(), name='index'),
    re_path('^index$', views.IndexView.as_view(), name='index'),
    re_path('^index/$', views.IndexView.as_view(), name='index'),
    re_path('^categories/$', views.CategoriesView.as_view(), name='categories'),
    re_path('^categories/(?P<category_slug>[\w-]+)/$', views.CategoryView.as_view(), name='category'),
]
