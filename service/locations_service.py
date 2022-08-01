from dao.locations_dao import LocationDao
from exception.locationnotfound import LocationNotFoundError
from exception.locationalreadyexisterror import LocationAlreadyExistError


class LocationService:
    @staticmethod
    def get_location(username):
        return LocationDao.get_location(username)

    @staticmethod
    def add_location(data, username):
        location = data["location"]
        add_success = LocationDao.add_location(location, username)
        if add_success:
            return add_success
        raise LocationAlreadyExistError(f"Hello, {username} {location} already exists in your favorite list.")

    @staticmethod
    def delete_location(data, username):
        location = data["location"]
        delete_success = LocationDao.delete_location(location, username)
        if delete_success:
            return f"{location} of {username} successfully deleted"
        raise LocationNotFoundError(f"{location} does not exist for the user {username} so delete unsuccessful")
