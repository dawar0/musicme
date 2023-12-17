import datetime
from models.utils.Tracking import Tracking


def SongModel(db):
    class Song(
        db.Model,
        Tracking,
    ):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(80), nullable=False)
        description = db.Column(db.String(120), nullable=False)
        tags = db.relationship("Tag", secondary="SongTag", back_populates="song")
        image = db.Column(db.String(120), nullable=False)
        song = db.Column(db.String(120), nullable=False)
        artistId = db.Column(db.Integer, db.ForeignKey("user.id"))
        artist = db.relationship(
            "User", back_populates="songs", foreign_keys=[artistId]
        )

        def __repr__(self):
            return f"{self.name} - {self.description}"

    return Song
