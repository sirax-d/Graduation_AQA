import allure
from allure_commons._allure import step
from jsonschema import validate

from superjob_project.schemas.schemas import vacancies_list_schema, vacancy_id_schema
from superjob_project.utils.base_requests import get_request
from tests.api.conftest import base_url_api


@allure.epic('API')
@allure.label("owner", "Authorized user with key")
@allure.feature("Checking response list vacancies on the site")
@allure.tag('ui', 'api')
@allure.severity('normal')
@allure.label('layer', 'api')
def test_get_vacancy():
    with step(f"GET {base_url_api + 'vacancies/'}"):
        response = get_request(url='vacancies/', period=1, keyword="Python")
        body = response.json()
        validate(body, vacancies_list_schema)
        assert response.status_code == 200


@allure.epic('API')
@allure.label("owner", "Authorized user with key")
@allure.feature("Checking information about the vacancy on the site")
@allure.tag('ui', 'api')
@allure.severity('normal')
@allure.label('layer', 'api')
def test_get_vacancy_with_id():
    with step(f"GET {base_url_api + 'vacancies/id'}"):
        response = get_request(url='vacancies/12284987')
        body = response.json()
        validate(body, vacancy_id_schema)
        assert response.status_code == 200
