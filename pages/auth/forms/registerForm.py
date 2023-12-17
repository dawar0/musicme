from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length, Optional, Regexp, EqualTo


class RegisterForm(FlaskForm):
    username = StringField(
        validators=[
            InputRequired(),
            Length(3, 20, message="Please provide a valid name"),
            Regexp(
                "^[A-Za-z][A-Za-z0-9_.]*$",
                0,
                "Usernames must have only letters, " "numbers, dots or underscores",
            ),
        ]
    )
    name = StringField(validators=[InputRequired(), Length(1, 64)])
    email = StringField(validators=[InputRequired(), Email(), Length(1, 64)])
    password = PasswordField(
        validators=[InputRequired(), Length(min=8, max=72)])
    confirmPassword = PasswordField(
        validators=[InputRequired(), Length(min=8, max=72),
                    EqualTo('password', message='Passwords must match')])
