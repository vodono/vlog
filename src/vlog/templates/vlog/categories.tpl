{% extends 'core/base.tpl' %}

{% block title %}Категории{% endblock %}

{% block breadcrumbs %}
    {{ super() }} / <a href="/categories/">Категории</a>
{% endblock %}

{% block content %}
    <h2>Список категорий влога:</h2>
    <hr><hr>
    {% for category in categories %}
        <h3><a href="/categories/{{ category.slug }}/">{{ category.title }}</a></h3>
        <hr>
    {% endfor %}
    <br>
{% endblock %}
