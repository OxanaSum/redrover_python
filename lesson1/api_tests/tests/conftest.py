import pytest
import requests
from lesson1.api_tests.services.case.data import create_case_dict

BASE_URL = "http://127.0.0.1:8000"

@pytest.fixture
def create_case():
    return requests.post(f"{BASE_URL}/testcases/", json=create_case_dict)

def get_case(id_):
    return requests.get(f"{BASE_URL}/testcases/{id_}")

def put_case(new_data, id_):
    return requests.put(f"{BASE_URL}/testcases/{id_}", json=new_data)

def delete_case(id_):
    return requests.delete(f"{BASE_URL}/testcases/{id_}")