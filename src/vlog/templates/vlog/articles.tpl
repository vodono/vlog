{% extends 'core/base.tpl' %}

{% block title %}Статьи{% endblock %}

{% block content %}
    <h2>Список статей влога:</h2>
    <hr><hr>
    {% for article in articles %}
        <h3><a href="/articles/{{ article.slug }}/">{{ article.title }}</a></h3>
        <hr>
    {% endfor %}
    <br>
{% endblock %}
