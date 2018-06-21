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

    {% block breadcrumbs %}
        <a href="/">Влог</a>
    {% endblock %}

        <br>
        <div class="container-fluid">
            {% block content %}
            {% endblock %}
        </div>
        <footer>
            <style>
                footer {background: grey}
            </style>
            <div class="footer-bg">
            <div class="copyright">
                <p><strong>Vlog experimental blog.</strong></p>
                <p>&copy; Santa</p>
            </div>
            </div>
        </footer>
    </body>
    <script src="{{ STATIC_URL }}js/bootstrap.min.js"></script>
</html>
