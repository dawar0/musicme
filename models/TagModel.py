def TagModel(db):
    class Tag(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(80), unique=True, nullable=False)
        song = db.relationship("Song", secondary="SongTag", back_populates="tags")

        def __repr__(self):
            return f"{self.name}"

    return Tag
