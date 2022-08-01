from dao.locations_dao import LocationDao
from exception.locationError import LocationError


class LocationService:
    @staticmethod
    def get_location(username):
        return LocationDao.get_location(username)

    @staticmethod
    def add_location(location_obj):
        update_location_object = LocationDao.add_location(location_obj)

        if update_location_object:
            return update_location_object.location_to_dict()
        raise LocationError(f"User with username {location_obj.username} was not found")

    @staticmethod
    def delete_location_by_id(username, location):
        if not LocationDao.delete_location_by_id(username, location):
            raise LocationError(f"Location {location} was not found")