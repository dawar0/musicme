import datetime
from db import db

from sqlalchemy.ext.declarative import declared_attr


class Tracking(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    createdAt = db.Column(
        db.DateTime,
        nullable=True,
        default=datetime.datetime.utcnow,
    )
    createdBy = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
    )
    updatedAt = db.Column(
        db.DateTime,
        nullable=True,
        default=datetime.datetime.utcnow,
    )
    updatedBy = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
    )
