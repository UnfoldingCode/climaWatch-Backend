from flask import Blueprint, request, session
from service.users_service import UsersService
from exception.userAlreadyExistError import UserAlreadyExistError
from exception.logInError import LogInError

uc = Blueprint("users_controller", __name__)


@uc.route("/users", methods=["GET", "POST"])
def get_users():
    if request.method == "GET":
        # return UsersService.get_users()
        return {"message":"Not allowed"}
    else:  # POST - create a new user *******************************************************
        try:
            data = request.get_json()
            return UsersService.create_user(data)
        except UserAlreadyExistError as e:
            # return {"message": str(e)}, 409
            return str(e), 409


@uc.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data["username"]
    password = data["password"]
    try:
        # Create an HTTP session object and associate with the user that is logged in with a key within the HTTP session
        # We add a key to the Http session object called "user_info" that contains the dictionary with all the user information.
        # Any subsequent request that is made by the client will be identified with the appropriate Http session object that contains that key
        user_info = UsersService.login(username, password)
        session["user_info"] = user_info["users"][0]
        print(session["user_info"])
        return user_info
    except LogInError as e:
        return {"message": str(e)}, 401


@uc.route("/loginstatus")
def loginstatus():
    if session.get("user_info"):
        return {
            "message": "You are logged in !!",
            "logged in user": session.get("user_info")
        }
    else:
        return "You are not logged in"


@uc.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return {"message": "Successfully logged out"}
