from django.urls import path, re_path

from vlog import views

urlpatterns = [
    re_path('^$', views.IndexView.as_view(), name='index'),
    re_path('^index$', views.IndexView.as_view(), name='index'),
    re_path('^index/$', views.IndexView.as_view(), name='index'),
]
