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
    {% for article in top_2_articles[:2] %}
        <h3><a href="/articles/{{ article.slug }}/">{{ article.title }}</a></h3>
        {{ article.description }}
        <hr>
    {% endfor %}
    <hr><br>

    {% for article in articles_page %}
        <h3><a href="/articles/{{ article.slug }}/">{{ article.title }}</a></h3>
        <hr>
    {% endfor %}

    <div class="pagination">
        <span class="step-links">
            {% if articles_page.has_previous() %}
                <a href="?page=1">&laquo; first</a>
                <a href="?page={{ articles_page.previous_page_number() }}">previous</a>
            {% endif %}

            <span class="current">
                Page {{ articles_page.number }} of {{ articles_page.paginator.num_pages }}.
            </span>

            {% if articles_page.has_next() %}
                <a href="?page={{ articles_page.next_page_number() }}">next</a>
                <a href="?page={{ articles_page.paginator.num_pages }}">last &raquo;</a>
            {% endif %}
        </span>
    </div>


    <br>
{% endblock %}


