{% extends 'core/base.tpl' %}

{% block title %}Индекс{% endblock %}

{% block content %}
    <h1>Влог</h1>
    <br>

    <h2 style="background-color:#98FB98"><a href="/categories/">Популярные категории:</a></h2>
    <hr><hr>
    {% for category in categories %}
        <h3><a href="/categories/{{ category.slug }}/">{{ category.title }}</a></h3>
        <hr>
    {% endfor %}
    <br>

    <h2 style="background-color:#98FB98"><a href="/articles/">Популярные статьи:</a></h2>
    <hr><hr>
    {% for article in articles %}
        <h3><a href="/articles/{{ article.slug }}/">{{ article.title }}</a></h3>
        <hr>
    {% endfor %}
    <br>

    <h2 style="background-color:#98FB98"><a href="/tags/">Популярные теги:</a></h2>
    <hr><hr>
    {% for tag in tags %}
        <h3><a href="/tags/{{ tag.slug }}/">{{ tag.title }}</a></h3>
        <hr>
    {% endfor %}

{% endblock %}
