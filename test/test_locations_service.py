import json

import pytest

import dao
import service
from dao.locations_dao import LocationDao
from exception.locationError import LocationError
from model.location_model import Location
from service.locations_service import LocationService


def test_get_location(mocker):
    def mock_get_location(username):
        return {
    "locations": [
        [
            3,
            "kareem11",
            "Dubai"
        ],
        [
            5,
            "kareem11",
            "Ottawa"
        ],
        [
            10,
            "kareem11",
            "Longo"
        ],
        [
            14,
            "kareem11",
            "Logo12"
        ],
        [
            15,
            "kareem11",
            "Logo122"
        ]
    ]
}
    mocker.patch('dao.locations_dao.LocationDao.get_location', mock_get_location)

    locations_service = LocationService()

    actual = locations_service.get_location('kareem11')

    assert actual == {
    "locations": [
        [
            3,
            "kareem11",
            "Dubai"
        ],
        [
            5,
            "kareem11",
            "Ottawa"
        ],
        [
            10,
            "kareem11",
            "Longo"
        ],
        [
            14,
            "kareem11",
            "Logo12"
        ],
        [
            15,
            "kareem11",
            "Logo122"
        ]
    ]
}


def test_add_location_positive(mocker):
    def mock_add_location(location_obj):
        return Location(16, location_obj.username, location_obj.location)

    mocker.patch('dao.locations_dao.LocationDao.add_location', mock_add_location)

    locations_service = LocationService()

    new_location = Location(None,'kareem11','Tokyo')

    actual = locations_service.add_location(new_location)

    test = Location(16, 'kareem11','Tokyo')
    assert actual == test.location_to_dict()


def test_add_location_negative(mocker):
    def mock_add_location(data):
       return None

    mocker.patch('dao.locations_dao.LocationDao.add_location', mock_add_location)

    locations_service = LocationService()

    new_location = Location(None,'kareem','Tokyo')

    with pytest.raises(LocationError) as e:
        actual = locations_service.add_location(new_location)

    assert str(e.value) == "User with username kareem was not found"


def test_delete_location_positive(mocker):
    def mock_delete_location(username, location):
        if username=="kareem11" and location=="Logo122":
            return True

    mocker.patch('service.locations_service.LocationService.delete_location_by_id', mock_delete_location)

    actual = service.locations_service.LocationService.delete_location_by_id("kareem11", "Logo122")

    assert actual == True


def test_delete_location_negative(mocker):
    def mock_delete_location(username, location):
        if username =="kareem11" and location=="Logo1222":
            return "Location Lfg was not found"

    mocker.patch('dao.locations_dao.LocationDao.delete_location_by_id', mock_delete_location)

    with pytest.raises(LocationError) as e:
        actual = service.locations_service.LocationService.delete_location_by_id("kareem1", "Lfg")

    assert str(e.value) == "Location Lfg was not found"
