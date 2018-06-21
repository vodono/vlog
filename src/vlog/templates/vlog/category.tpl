{% extends 'core/base.tpl' %}

{% block title %}Категория: {{ category.title }}{% endblock %}

{% block breadcrumbs %}
    {{ super() }}
    / <a href="/categories/">Категории</a>
    / <a href="/categories/{{ category.slug }}"> {{ category.title }} </a>
{% endblock %}

{% block content %}
    <h2>Категория: {{ category.title }}</h2>
    <hr><hr>
    {% for article in top_articles[:2] %}
        <h3><a href="/articles/{{ article.slug }}/">{{ article.title }}</a></h3>
        {{ article.description }}
        <hr>
    {% endfor %}
    <hr><br>
    {% for article in top_articles %}
        <h3><a href="/articles/{{ article.slug }}/">{{ article.title }}</a></h3>
        <hr>
    {% endfor %}
    <br>
{% endblock %}
