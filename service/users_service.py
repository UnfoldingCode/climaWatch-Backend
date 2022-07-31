from dao.users_dao import UsersDao
from utility.users_utility import UserFormat
from exception.userAlreadyExistError import UserAlreadyExistError


class UsersService:
    @staticmethod
    def get_users():
        users_received_from_dao = UsersDao.get_users()
        return UserFormat.format_users(users_received_from_dao)

    @staticmethod
    def create_user(data):
        new_user = UsersDao.create_user(data)
        if new_user:
            return new_user
        raise UserAlreadyExistError("Username or/and email already exist !!!")

    @staticmethod
    def login(username, password):
        return f"Login at Service layer {username} {password}"