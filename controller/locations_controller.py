from flask import Blueprint, request, session
from service.locations_service import LocationService

lc = Blueprint("location_controller", __name__)


@lc.route("/locations/<username>", methods=["GET"])
def get_location(username):
    if session.get("user_info"):
        if session["user_info"]["username"] == username:
            return LocationService.get_location(username)
    else:
        return "Please log in first!!", 401
