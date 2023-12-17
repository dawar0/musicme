from flask import (
    Blueprint,
    jsonify,
    request,
    Flask,
    render_template,
    flash,
    redirect,
    url_for,
)
from db import User, Song, db

from utils.renderWithContext import renderWithContext
from flask import request
from flask_login import login_required, current_user

index = Blueprint("index", __name__, template_folder="templates")


@index.route("/")
def home():
    songs = Song.query.limit(10).all()
    trendingSongs = Song.query.limit(10).all()
    latestSongs = Song.query.order_by(Song.createdAt.desc()).limit(10).all()

    print([song.artist.name for song in songs])

    sections = [
        {
            "name": "Latest",
            "songs": latestSongs,
        },
        {
            "name": "Trending",
            "songs": trendingSongs,
        },
    ]

    return renderWithContext(
        "admin.html",
        sections=sections,
    )
