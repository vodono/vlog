{% extends 'core/base.tpl' %}
{% block content %}

    {% if form.errors %}
        <p>Your username and password didn't match. Please try again.</p>
    {% endif %}
    <div class="row">
    <div class="col-md-4">&nbsp;</div>
    <div class="col-md-4">
        <form method="post" action="{{ url('login') }}">
            {% csrf_token %}
            <div class="form-group">
                <label for="id_{{ form.username.name }}">{{ form.username.label_tag() }}</label>
                <div class="input-group">
                    <div class="input-group-prepend">
                        <span class="input-group-text" id="inputGroupPrepend2">@</span>
                    </div>
                    <input type="text" class="form-control" id="id_{{ form.username.name }}" name="{{ form.username.name }}" placeholder="Username" aria-describedby="inputGroupPrepend2" required>
                </div>
            </div>
            <div class="form-group">
                <label for="id_{{ form.password.name }}">{{ form.password.label_tag() }}</label>
                <input type="password" id="id_{{ form.password.name }}" name="{{ form.password.name }}" class="form-control">
            </div>
            <button class="btn btn-primary" type="submit">{{ _('Submit') }}</button>
            <input type="hidden" name="next" value="{{ next }}" />
        </form>
    </div>
    </div>
{% endblock %}
