from dao.locations_dao import LocationDao


class LocationService:
    @staticmethod
    def get_location(username):
        return LocationDao.get_location(username)

    @staticmethod
    def add_location(data, username):
        return LocationDao.add_location(data, username)
