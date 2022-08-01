from flask import Flask
from flask_session import Session
from flask_cors import CORS

from controller.users_controller import uc
from controller.locations_controller import lc

if __name__ == "__main__":
    app = Flask(__name__)
    CORS(app,
         supports_credentials=True)  # It instructs our webserver to tell browser that any origin is allowed. By origin, we mean the source
    # where the HTML, CSS and JS are originating from
    # pip install Flask-Session
    # https://flask-cors.readthedocs.io/en/latest/

    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)

    app.register_blueprint(uc)
    app.register_blueprint(lc)

    app.run(port=6060, debug=True)
