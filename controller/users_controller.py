from flask import Blueprint, request, session
from service.users_service import UsersService
from exception.userAlreadyExistError import UserAlreadyExistError

uc = Blueprint("users_controller", __name__)


@uc.route("/users", methods=["GET", "POST"])
def get_users():
    if request.method == "GET":
        return UsersService.get_users()
    else:  # POST - create a new user
        try:
            data = request.get_json()
            return UsersService.create_user(data)
        except UserAlreadyExistError as e:
            return {"message": str(e)}


@uc.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data["username"]
    password = data["password"]
    # Create an HTTP session object and associate with the user that is logged in with a key within the HTTP session
    # We add a key to the Http session object called "user_info" that contains the dictionary with all the user information.
    # Any subsequent request that is made by the client will be identified with the appropriate Http session object that contains that key
    return UsersService.login(username, password)
