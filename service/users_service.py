from dao.users_dao import UsersDao


class UsersService:
    @staticmethod
    def get_users():
        return UsersDao.get_users()
