from flask import render_template
from flask_login import current_user


def renderWithContext(template, user=current_user, **kwargs, ):
    return render_template(template, user=user, ** kwargs)
