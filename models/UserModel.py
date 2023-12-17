from models.utils.Tracking import Tracking
from flask_login import UserMixin


def UserModel(
    db,
):
    class User(db.Model, UserMixin):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(80), unique=True, nullable=False)
        email = db.Column(db.String(120), unique=True, nullable=False)
        username = db.Column(db.String(120), unique=True, nullable=False)
        password = db.Column(db.String(120), unique=True, nullable=False)
        isAdmin = db.Column(db.Boolean, nullable=True, default=False)
        image = db.Column(db.String(120), unique=True, nullable=True)

        songs = db.relationship(
            "Song", back_populates="artist", foreign_keys="Song.artistId"
        )

        def __repr__(self):
            return f"{self.name} - {self.email}"

    return User
