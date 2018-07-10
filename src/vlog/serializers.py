from django.contrib.auth import get_user_model
from rest_framework import serializers
from vlog.models import Category, Article, Tag


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'username',
        )


class CategorySerializer(serializers.ModelSerializer):
    author = UserSerializer(required=True)

    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'slug',
            'created',
            'updated',
            'image',
            'description',
            'author'
        )


class ArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=True)
    author = UserSerializer(required=True)

    class Meta:
        model = Article
        fields = (
            'id',
            'title',
            'slug',
            'created',
            'updated',
            'content',
            'image',
            'description',
            'author',
            'category',
            'publication_date'
        )


class TagSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(required=True, many=True)

    class Meta:
        model = Tag
        fields = (
            'id',
            'title',
            'slug',
            'created',
            'updated',
            'articles'
        )
