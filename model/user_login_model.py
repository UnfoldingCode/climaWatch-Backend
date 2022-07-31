class UserLogin:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

    def user_to_dict(self):
        return {
            "username": self.username,
            "name": self.name,
            "email": self.email
        }
