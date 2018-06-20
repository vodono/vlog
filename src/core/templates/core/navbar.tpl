<nav class="navbar navbar-dark bg-primary">
    <span class="navbar-text">
        <a class="navbar-brand" href="{{ url('vlog:index') }}">{{ _('Vlog') }}</a>
        <a class="navbar-brand" href="{{ url('vlog:categories') }}">{{ _('Categories') }}</a>
        <a class="navbar-brand" href="{{ url('vlog:tags') }}">{{ _('Tags') }}</a>
        <a class="navbar-brand" href="{{ url('vlog:articles') }}">{{ _('Articles') }}</a>
    </span>
    {% if user.is_authenticated %}
        <span class="navbar-text">
            {{ _('Hello') }}, {{ user.username }}!&nbsp;<a href="{{ url('logout') }}">{{ _('GTFO!') }}</a>
        </span>
    {% endif %}
</nav>
