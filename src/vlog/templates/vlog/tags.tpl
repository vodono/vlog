{% extends 'core/base.tpl' %}

{% block title %}Теги{% endblock %}

{% block breadcrumbs %}
    {{ super() }} / <a href="/tags/">Список тегов</a>
{% endblock %}

{% block content %}
    <h2>Список тегов влога:</h2>
    <hr><hr>
    {% for tag in tags %}

        <h3 style="background-color:#98FB98"><a href="/tags/{{ tag.slug }}/">{{ tag.title }}</a></h3>

        {% set count = [3] %}
        {% for article in articles_by_tag if article.tags == tag.id and count[0] > 0 %}
            <h5><a href="/articles/{{ article.slug }}/">{{ article.title }}</a></h5>
            {% if count.append(count.pop() - 1) %} {% endif %}
        {% endfor %}
        <hr>
    {% endfor %}
    <br>
{% endblock %}
