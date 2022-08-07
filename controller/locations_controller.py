from flask import Blueprint, request, session
from service.locations_service import LocationService
from exception.locationnotfound import LocationNotFoundError
from exception.locationalreadyexisterror import LocationAlreadyExistError

lc = Blueprint("location_controller", __name__)


@lc.route("/locations/<username>", methods=["GET", "POST", "DELETE"])
def get_location(username):
    if session.get("user_info"):
        if session["user_info"]["username"] == username:
            if request.method == "GET":
                return LocationService.get_location(username)
            #     if session.get("user_info"):
            #         if session["user_info"]["username"] == username:
            #             return LocationService.get_location(username)

            elif request.method == "POST":  # ***************** POST - add new location
                try:
                    data = request.get_json()
                    return LocationService.add_location(data, username)
                except LocationAlreadyExistError as e:
                    return {"message": str(e)}

            else:  # ***************** DELETE - delete existing location
                try:
                    data = request.get_json()
                    return LocationService.delete_location(data, username)
                except LocationNotFoundError as e:
                    return {"message": str(e)}, 404
    else:
        return "Please log in first!!", 401



