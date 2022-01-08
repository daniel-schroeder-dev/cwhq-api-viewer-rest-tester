from flask import Flask, jsonify, request, make_response
from functools import wraps
from json import loads

from db import init_db
from user import User

app = Flask(__name__)

# http://127.0.0.1:5000/


def cors(view_func):
    @wraps(view_func)
    def wrapper(**kwargs):
        if request.method == "OPTIONS":
            response = make_response()
            response.headers.add("Access-Control-Allow-Origin", "*")
            response.headers.add("Access-Control-Allow-Headers", "*")
            response.headers.add("Access-Control-Allow-Methods", "*")
            return response

        return view_func(**kwargs)

    return wrapper


@app.route("/", methods=("GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"))
@cors
def index():
    json_data = request.get_json()
    if json_data:
        json_data = loads(json_data)

    response_data = {
        "message": "Hello from Flask!",
        "method": request.method,
        "args": request.args,
        "form-data": request.form,
        "json-data": json_data,
    }
    response = jsonify(response_data)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/init-db")
@cors
def build_db():
    init_db()
    response = jsonify({"message": "DB recreated!"})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/users", methods=("GET", "OPTIONS"))
@cors
def get_users():
    response_data = [user.__dict__ for user in User.load_all_users()]
    response = jsonify(response_data)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response