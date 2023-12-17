import importlib
import models
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


User = importlib.import_module("models.UserModel").UserModel(db)
Song = importlib.import_module("models.SongModel").SongModel(db)
SongTag = importlib.import_module("models.SongTagModel").SongTagModel(db)
Tag = importlib.import_module("models.TagModel").TagModel(db)
