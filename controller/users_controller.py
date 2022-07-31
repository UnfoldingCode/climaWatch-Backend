from flask import Blueprint, request, session
from service.users_service import UsersService

uc = Blueprint("users_controller", __name__)


@uc.route("/users", methods=["GET"])
def get_users():
    if (request.method=="GET"):
        return UsersService.get_users()

