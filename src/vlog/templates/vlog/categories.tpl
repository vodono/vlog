{% extends 'core/base.tpl' %}

{% block title %}Категории{% endblock %}

{% block content %}
    <h1>Влог</h1>
    <br>

    <h2>Все категории:</h2>
    {% for category in categories %}
        <h3><a href="/categories/{{ category.slug }}/">{{ category.title }}</a></h3>
        <hr>
    {% endfor %}
    <br>
{% endblock %}
