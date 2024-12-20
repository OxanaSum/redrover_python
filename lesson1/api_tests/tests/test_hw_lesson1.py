import requests
from lesson1.api_tests.services.case.data import create_case_dict
from lesson1.api_tests.tests import conftest


def test_create_case(create_case):
    case_response = create_case

    assert case_response.status_code == 200
    assert case_response.json()["name"] == create_case_dict["name"]


def test_get_case(create_case):
    case_create_response = create_case
    case_id = case_create_response.json()["id"]
    case_get_response = conftest.get_case(case_id)

    assert case_get_response.status_code == 200
    assert case_get_response.json()["name"] == case_create_response.json()["name"]


def test_put_case(create_case):
    new_data = {
        "id": "8",
        "name": "Новое тестовое задание",
        "description" : "Описание нового тестового задания",
        "priority": "средний",
        "steps": ["Step1", "Step2", "Step3"],
        "expected_result": "Задание выполнено",
    }

    case_create_response = create_case
    case_id = case_create_response.json()["id"]
    new_response = conftest.put_case(new_data, case_id)

    assert new_response.json()["name"] == new_data["name"]


def test_delete_case(create_case):
    case_create_response = create_case
    case_id = case_create_response.json()["id"]
    response = conftest.delete_case(case_id)

    assert response.status_code == 200
    assert response.json()["detail"] == "Test case deleted."
