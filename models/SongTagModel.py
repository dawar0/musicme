def SongTagModel(db):
    class SongTag(db.Model):
        __tablename__ = "SongTag"
        id = db.Column(db.Integer, primary_key=True)
        show_id = db.Column(db.Integer, db.ForeignKey("song.id"), nullable=False)
        tag_id = db.Column(db.Integer, db.ForeignKey("tag.id"), nullable=False)

        def __repr__(self):
            return f"{self.show_id} - {self.tag_id}"

    return SongTag
