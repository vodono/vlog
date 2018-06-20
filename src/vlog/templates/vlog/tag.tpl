{% extends 'core/base.tpl' %}

{% block title %}Тег: {{ tag.title }}{% endblock %}

{% block content %}
    <h2>Тег: {{ tag.title }}</h2>
    <hr><hr>
    {% for article in articles %}
        <h3><a href="/articles/{{ article.slug }}/">{{ article.category }}: {{ article.title }}</a></h3>
        <hr>
    {% endfor %}
    <br>
{% endblock %}
