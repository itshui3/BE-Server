from flask import Blueprint, request, jsonify
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from .models import Users
from datetime import datetime, timedelta
from . import db
import os
import json
import jwt
from dotenv import load_dotenv
from .dump import json_response

load_dotenv()

auth = Blueprint("auth", __name__)

JWT_SECRET = os.environ.get("SECRET")
JWT_ALGORITHM = "HS256"
JWT_EXP_DELTA_SECONDS = 2000000


@auth.route("/")
def get_index():
    return "hello"


@auth.route("/login/", methods=["POST"])
def login():
    req = request.json

    user = Users.query.filter_by(username=req["username"]).first()

    if not user or not check_password_hash(user.password, req["password"]):
        return "Sorry, no soup for you!"
    else:
        payload = {
            "user_id": user.id,
            "exp": datetime.utcnow() + timedelta(seconds=JWT_EXP_DELTA_SECONDS),
        }

        jwt_token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)
        return json_response({"key": jwt_token.decode("ascii")})


@auth.route("/registration/", methods=["POST"])
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

        payload = {
            "user_id": current_user.id,
            "exp": datetime.utcnow() + timedelta(seconds=JWT_EXP_DELTA_SECONDS),
        }

        jwt_token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)
        return json_response({"key": jwt_token.decode("ascii")})

    else:
        return "Passwords don't match"
