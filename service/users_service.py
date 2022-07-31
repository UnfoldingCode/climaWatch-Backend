from dao.users_dao import UsersDao
from utility.users_utility import UserFormat


class UsersService:
    @staticmethod
    def get_users():
        users_received_from_dao = UsersDao.get_users()
        return UserFormat.format_users(users_received_from_dao)
