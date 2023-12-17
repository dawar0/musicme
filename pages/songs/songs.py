from flask import Blueprint, jsonify, request, Flask, render_template, flash
from db import User, Song, db
from flask_login import login_required, current_user
from utils.renderWithContext import renderWithContext
from pages.songs.forms.addSongForm import AddSongForm
from datetime import datetime

songs = Blueprint("songs", __name__, template_folder="templates")


@songs.route("/songs/<int:id>")
def getSong(id):
    song = Song.query.get(id)
    return jsonify(song.serialize())


@songs.route("/songs/add", methods=["GET", "POST"])
@login_required
def addSong():
    if request.method == "GET":
        form = AddSongForm()
        print(form.artist)
        return renderWithContext(
            "addSong.html",
            form=form,
            buttonAction="Add Song",
            user=current_user,
        )
    elif request.method == "POST":
        date = datetime.now().strftime("%H%M%S")
        files = request.files
        songFile = files["song"]
        imageFile = files["image"]
        songFilePath = f"static/songs/{request.form['name']}{date}.{songFile.filename.split('.')[-1]}".replace(
            " ", "_"
        )
        imageFilePath = f"static/images/{request.form['name']}{date}.{imageFile.filename.split('.')[-1]}".replace(
            " ", "_"
        )
        songFile.save(songFilePath)
        imageFile.save(imageFilePath)

        show = Song(
            name=request.form["name"],
            description=request.form["description"],
            image=imageFilePath,
            song=songFilePath,
            artist=current_user,
        )
        db.session.add(show)
        db.session.commit()
        flash("Song added successfully", "success")
        form = AddSongForm()
        return renderWithContext(
            "addSong.html",
            form=form,
            buttonAction="Add Song",
            user=current_user,
        )
