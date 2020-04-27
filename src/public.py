from flask import Blueprint

public = Blueprint("public_routes", __name__)

@public.route('/')
def get_index():
    return "hello"