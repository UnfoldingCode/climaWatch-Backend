from model.user_model import User
from model.user_login_model import UserLogin


class UserFormat:
    @staticmethod
    def format_users(allUsers):
        users = allUsers["users"]
        users_formatted = []
        for user in users:
            s_num = user[0]
            username = user[1]
            name = user[2]
            email = user[3]
            password = user[4]
            user_dict = User(s_num, username, name, email, password).user_to_dict()
            users_formatted.append(user_dict)
        return {"users": users_formatted}

    @staticmethod
    def format_single_user(userDetails):
        user = userDetails["users"]
        user_formatted = []
        username = user[1]
        name = user[2]
        email = user[3]

        user_dict = UserLogin(username, name, email).user_to_dict()
        user_formatted.append(user_dict)
        return {"users": user_formatted}
