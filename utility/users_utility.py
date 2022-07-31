from model.user_model import User


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

