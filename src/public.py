from flask import Blueprint, request, jsonify
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from .models import Users
from . import db
import os
import json

public = Blueprint("public_routes", __name__)

secret = os.environ.get("DATABASE_URL")


@public.route("/")
def get_index():
    return "hello"


@public.route("/login", methods=["POST"])
def login():
    return request


@public.route("/registration/")
def register():
    return "hello"


@public.route("/registration/", methods=["POST"])
def register_request():
    req = request.json

    user = Users.query.filter_by(username=req["username"]).first()

    # if a user is found, return an error
    if user:
        return "Username address already exists"

    # create new user with the form data. Hash the password so plaintext version isn't saved.
    if req["password1"] == req["password2"]:
        new_user = Users(
            username=req["username"],
            password=generate_password_hash(req["password1"], method="sha256"),
        )

        # add the new user to the database
        db.session.add(new_user)
        db.session.commit()
        current_user = Users.query.filter_by(username=req["username"]).first()
        print(current_user.username)
        return f"Yay! Congratz, {current_user.username}! 🚀"

    else:
        return "Passwords don't match"
