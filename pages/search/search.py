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

search = Blueprint("search", __name__, template_folder="templates")


@search.route("/search")
def searchSongs():
    searchTerm = request.args.get("searchTerm")
    songs = Song.query.filter(Song.name.ilike(f"%{searchTerm}%")).limit(100).all()
    print(songs)

    return renderWithContext(
        "search.html",
        songs=songs,
    )
