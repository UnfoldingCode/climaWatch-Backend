from flask import Blueprint, request, session

uc = Blueprint("users_controller", __name__)


@uc.route("/")
def users():
    return "Users at controller"
