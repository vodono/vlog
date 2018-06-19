{% extends 'core/base.tpl' %}

{% block title %}Индекс{% endblock %}

{% block content %}
    <h1>Влог</h1>
    <br>

    <h2><a href="categories/">Популярные категории:</a></h2>
    {% for category in categories %}
        <h3><a href="categories/{{ category.slug }}/">{{ category.title }}</a></h3>
        <hr>
    {% endfor %}
    <br>

    <h2><a href="articles/">Популярные статьи:</a></h2>
    {% for article in articles %}
        <h3><a href="articles/{{ article.slug }}/">{{ article.title }}</a></h3>
        <hr>
    {% endfor %}
    <br>

    <h2><a href="tags/">Лучшие теги</a></h2>
    {% for tag in tags %}
        <h3><a href="tags/{{ tag.slug }}/">{{ tag.title }}</a></h3>
        <hr>
    {% endfor %}

{% endblock %}
