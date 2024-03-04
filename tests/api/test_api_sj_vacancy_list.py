import os

import allure
from allure_commons._allure import step
from dotenv import load_dotenv
from jsonschema import validate

from superjob_project.data.api.schemas import get_vacancies_schema
from superjob_project.utils.base_requests import get_request

load_dotenv()
base_url_api = os.getenv("BASE_URL_API")


@allure.epic('API')
@allure.label("owner", "Autohrized user with key")
@allure.feature("Checking response list vacancies on the site")
@allure.tag('ui', 'api')
@allure.severity('normal')
@allure.label('layer', 'api')
def test_get_vacancy():
    with step(f"GET {base_url_api}"):
        response = get_request(url='vacancies/', period=1, keyword="Python")
        body = response.json()
        validate(body, get_vacancies_schema)
        assert response.status_code == 200
