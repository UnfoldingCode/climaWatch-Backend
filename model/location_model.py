class Location:
    def __init__(self, location_id, users_username, location):
        self.location_id = location_id
        self.username = users_username
        self.location = location

    def location_to_dict(self):
        return {
            "Location_id": self.location_id,
            "Username": self.username,
            "Location": self.location
        }
