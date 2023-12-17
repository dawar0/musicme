from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length, Optional


class LoginForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Email(), Length(1, 64)])
    password = PasswordField(
        validators=[InputRequired(), Length(min=8, max=72)])
