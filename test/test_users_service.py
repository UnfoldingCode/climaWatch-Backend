import pytest
import json
from dao.users_dao import UsersDao
from exception.logInError import LogInError
from service.users_service import UsersService
from exception.userAlreadyExistError import UserAlreadyExistError
from utility.users_utility import UserFormat


def test_get_users(mocker):
        def mock_get_users():
            return {"users": [(1, 'john999', 'John','HBO2@netflix.com', 'password'), (2, 'bob222', 'Bob','HBO6@netflix.com', 'password'), (3, 'lean888', 'Lean','HBO16@netflix.com', 'password')]}

        mocker.patch('dao.users_dao.UsersDao.get_users', mock_get_users)

        users_service = UsersService()

        actual = users_service.get_users()

        assert actual == {
            "users": [{
                "email": "HBO2@netflix.com",
                "name": "John",
                "password": "password",
                "s_num": 1,
                "username": "john999"
            },
                {
                    "email": "HBO6@netflix.com",
                    "name": "Bob",
                    "password": "password",
                    "s_num": 2,
                    "username": "bob222"
                },
                {
                    "email": "HBO16@netflix.com",
                    "name": "Lean",
                    "password": "password",
                    "s_num": 3,
                    "username": "lean888"
                }
            ]
        }


def test_create_user_positive(mocker):
    def mock_create_user(data):
        return "New user successfully created"

    mocker.patch('dao.users_dao.UsersDao.create_user', mock_create_user)

    users_service = UsersService()

    x='{"username": "willow12","name": "Willow","email": "abc12@skyline.com","password": "password"}'

    y = json.loads(x)

    actual = users_service.create_user(y)

    assert actual == 'New user successfully created'


def test_create_user_negative(mocker):
    def mock_create_user(data):
        return False

    mocker.patch('dao.users_dao.UsersDao.create_user', mock_create_user)

    users_service = UsersService()

    x='{"username": "willow11","name": "Willo","email": "abc12@skyline.com","password": "password"}'

    y = json.loads(x)

    with pytest.raises(UserAlreadyExistError) as e:
        actual = users_service.create_user(y)

    assert str(e.value) == "Username or/and email already exist !!!"


def test_login_user_positive(mocker):
    def mock_login_user(username,password):
        return {'users': (3, 'kareem11', 'Kareem', 'abc3@skyline.com', 'password')}

    mocker.patch('dao.users_dao.UsersDao.login', mock_login_user)

    users_service = UsersService()

    actual = users_service.login('kareem11', 'password')

    assert actual == {
    "users": [
        {
            "email": "abc3@skyline.com",
            "name": "Kareem",
            "username": "kareem11"
        }
    ]
}


def test_login_user_negative(mocker):
    def mock_login_user(username, password):
        return False

    mocker.patch('dao.users_dao.UsersDao.login', mock_login_user)

    users_service = UsersService()


    with pytest.raises(LogInError) as e:
        actual = users_service.login(" ", " ")

    assert str(e.value) == "Username and Password does not match. Please try again with correct credentials !!!"

