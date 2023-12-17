from app import db
from app import application
from db import User, Song
from app import bcrypt
from faker import Faker
import random

import requests

with application.app_context():
    db.drop_all()
    db.create_all()
    user = User(
        username="admin",
        email="",
        name="Administrator",
        isAdmin=True,
        password=bcrypt.generate_password_hash("admin123456").decode("utf-8"),
    )

    users = []
    for _ in range(0, 5):
        users.append(
            User(
                username=Faker().user_name(),
                email=Faker().email(),
                name=Faker().user_name(),
                isAdmin=False,
                password=bcrypt.generate_password_hash("user123456").decode("utf-8"),
            )
        )

    db.session.add(user)
    doggyImage = []
    for _ in range(0, 10):
        response = requests.get("https://dog.ceo/api/breeds/image/random")
        data = response.json()

        if data["status"] == "success":
            print(data["message"])
            doggyImage.append(data["message"])
        else:
            print("Failed to fetch image")

    for i in range(0, 10):
        db.session.add(
            Song(
                name=f"Song {i}",
                description=f"Song {i} description",
                image=doggyImage[i],
                song=f"https://www.soundhelix.com/examples/mp3/SoundHelix-Song-{i}.mp3",
                artist=users[random.randint(0, len(users) - 1)],
            )
        )

    db.session.commit()
