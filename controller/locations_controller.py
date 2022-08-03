from flask import Blueprint, request, session

from exception.locationError import LocationError
from service.locations_service import LocationService
from model.location_model import Location
lc = Blueprint("location_controller", __name__)


@lc.route("/locations/<username>", methods=["GET"])
def get_location(username):
    if session.get("user_info"):
        if session["user_info"]["username"] == username:
            return LocationService.get_location(username)
    else:
        return "Please log in first!!", 401

@lc.route("/locations/<username>", methods=["POST"])
def add_location(username):
    json_dict = request.get_json()
    if session.get("user_info"):
        if session["user_info"]["username"] == username:
            return LocationService.add_location(Location(None, username, json_dict['location']))
    else:
        return "Please log in first!!", 401


@lc.route("/locations/<username>", methods=["DELETE"])
def delete_location_by_id(username):
    try:
        json_dict = request.get_json()
        LocationService.delete_location_by_id(username, json_dict['location'])
        return{
            "message": f"User with username{username} with location {json_dict['location']} was successfully deleted"
        }, 200
    except LocationError as e:
        return {
            "message": str(e)
        }, 401