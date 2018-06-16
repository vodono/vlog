from django.contrib import admin
from vlog import models
from vlog import forms


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    form = forms.ArticleForm


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    form = forms.CategoryForm


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    form = forms.TagForm


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    form = forms.CommentForm
