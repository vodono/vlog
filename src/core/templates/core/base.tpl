<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" href="{{ STATIC_URL }}css/bootstrap.min.css">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>{% block title %}{% endblock %}</title>
    </head>
    <body>
        {% block navbar %}
            {% include 'core/navbar.tpl' %}
        {% endblock %}

        {% load django_bootstrap_breadcrumbs %}
        {% block breadcrumbs %}
            {% clear_breadcrumbs %}
            {% breadcrumb "Home" "/" %}
        {% endblock %}

        {% block content_breadcrumbs %}
            {% render_breadcrumbs %}
        {% endblock %}

        <br>
        <div class="container-fluid">
            {% block content %}
            {% endblock %}
        </div>
    </body>
    <script src="{{ STATIC_URL }}js/bootstrap.min.js"></script>
</html>
