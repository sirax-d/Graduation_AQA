import allure
from allure_commons._allure import step
from jsonschema import validate

from superjob_project.schemas.schemas import invalid_token_schema, invalid_unblock_company_schema
from superjob_project.utils.base_requests import put_request, delete_request
from tests.api.conftest import base_url_api


@allure.epic('API')
@allure.label("owner", "Unauthorized key")
@allure.feature("Invalid request authorization code to the site")
@allure.tag('ui', 'api')
@allure.severity('normal')
@allure.label('layer', 'api')
def test_invalid_acces_token():
    with step(f"PUT {base_url_api}"):
        response = put_request(url='oauth2/access_token/')
        body = response.json()
        validate(body, invalid_token_schema)
        assert 'error' in body
        assert 'message' in body['error'] and 'Неверно передан параметр code' in body['error']['message']
        assert response.status_code == 401


@allure.epic('API')
@allure.label("owner", "Unauthorized key and login")
@allure.feature("Checking not-exist method on the site")
@allure.tag('ui', 'api')
@allure.severity('normal')
@allure.label('layer', 'api')
def test_unblock_company():
    id = 1000000
    with step(f"DELETE {base_url_api}"):
        response = delete_request(url=f'clients/{id}/block/')
        body = response.json()
        validate(body, invalid_unblock_company_schema)
        assert response.status_code != 200
        assert 'error' in body
        assert 'message' in body[
            'error'] and 'Неправильно набран адрес, или такой страницы "2.0/clients/1000000/block" на сайте больше не существует' in \
               body['error']['message']
