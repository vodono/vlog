{% extends 'core/base.tpl' %}

{% block title %} {{ article.title }} {% endblock %}

{% block breadcrumbs %}
    {{ super() }}
    / <a href="/articles/">Статьи</a>
    / <a href="/articles/{{ article.slug }}"> {{ article.title }} </a>
{% endblock %}

{% block content %}
    <h2>{{ article.title }}</h2>
    <hr><br>

    <img src="{{ article.image.url }}"/>
    <br>
    {% autoescape off %} {{ article.content }} {% endautoescape %}
    <br>
{% endblock %}
