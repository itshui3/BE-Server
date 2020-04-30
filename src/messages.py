from flask import Blueprint, request, jsonify
import jwt
import os
from . import db, pusher_client
from .models import Messages, Users
from .dump import json_response
import json

messages = Blueprint("messages", __name__)

JWT_SECRET = os.environ.get("SECRET")


@messages.route("/messages/", methods=["POST"])
def post_message():
    userId = jwt.decode(request.headers["token"], JWT_SECRET)["user_id"]
    user = db.session.query(Users).filter_by(id=userId)

    req = request.json

    new_message = Messages(username=req["username"], message=req["message"],)

    # add the new message to the database
    added_message = db.session.add(new_message)
    db.session.commit()
    all_messages = db.session.query(Messages).all()
    last_message = all_messages[-1]
    print("added message:", last_message.username)
    returned_message = {
        "id": last_message.id,
        "username": last_message.username,
        "message": last_message.message,
    }

    pusher_client.trigger(
        "chat-room", "message", {"username": req["username"], "message": req["message"]}
    )

    return returned_message


@messages.route("/messages/", methods=["GET"])
def get_posts():
    userId = jwt.decode(request.headers["token"], JWT_SECRET)["user_id"]
    # messages = db.session.query(Messages).all()
    messages = db.session.query(Messages).all()

    message_arr = []
    for message in messages:
        # print(message.username)
        message_arr.append(
            {"id": message.id, "username": message.username, "message": message.message}
        )
    print(jsonify(message_arr.reverse()))
    # return json.dumps(messages)
    # message_arr = []
    # for message in messages:
    #     message_arr.append(
    #         jsonify({"username": message.username, "message": message.message})
    #     )
    # print(jsonify(message_arr))
    # print(jsonify(message_arr))
    print("len", len(message_arr))
    return jsonify(message_arr[slice(0, 50)])
