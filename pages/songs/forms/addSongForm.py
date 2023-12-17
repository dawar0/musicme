from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    TextAreaField,
    SubmitField,
    SelectField,
    DateField,
    TimeField,
    FileField,
)
from wtforms.validators import DataRequired, ValidationError
from flask_wtf.file import FileField, FileAllowed, FileRequired


def LessThan(form, field):
    if form.endTime.data < form.time.data:
        raise ValidationError("End time must be after start time")


class AddSongForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    artist = StringField(
        "Artist",
        validators=[DataRequired()],
    )
    description = TextAreaField("Description", validators=[DataRequired()])
    image = FileField(
        "Image",
        validators=[FileRequired(), FileAllowed(["jpg", "png"], "Images only!")],
    )
    song = FileField(
        "Song",
        validators=[FileRequired(), FileAllowed(["mp3", "wav"], "Songs only!")],
    )

    submit = SubmitField("Submit")
