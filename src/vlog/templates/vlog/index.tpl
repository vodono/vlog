{% extends 'core/base.tpl' %}

{% block title %}Index{% endblock %}

{% block content %}
    <h1>Django Unchained Blog</h1>
    <br>

    <h2>Popular categories</h2>
    {% for category in categories %}
        <h2><a href="categories/{{ category.title.lower }}/">{{ category.title }}</a></h2>
        <hr>
    {% endfor %}
    <br>

    <h2>Popular articles</h2>
    {% for article in articles %}
        <h2><a href="articles/{{ article.title.lower }}/">{{ article.title }}</a></h2>
        <hr>
    {% endfor %}
    <br>

    <h2>Active tags</h2>
    {% for tag in tags %}
        <h2><a href="tags/{{ tag.title.lower }}/">{{ tag.title }}</a></h2>
        <hr>
    {% endfor %}

{% endblock %}
