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

