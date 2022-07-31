class User:
    def __init__(self, s_num, username, name, email, password):
        self.s_num = s_num
        self.username = username
        self.name = name
        self.email = email
        self.password = password

    def user_to_dict(self):
        return {
            "s_num": self.s_num,
            "username": self.username,
            "name": self.name,
            "email": self.email,
            "password": self.password
        }
