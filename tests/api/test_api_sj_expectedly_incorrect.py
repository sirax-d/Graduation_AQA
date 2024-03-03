import os
import allure
from allure_commons._allure import step
from dotenv import load_dotenv
from superjob_project.utils.base_requests import put_request, delete_request



load_dotenv()
base_url_api = os.getenv("BASE_URL_API")



@allure.epic('API')
@allure.label("owner", "Unauthorized key")
@allure.feature("Unvalid request authorization code to the site")
@allure.tag('ui', 'api')
@allure.severity('normal')
@allure.label('layer', 'api')
def test_invalid_acces_token():
    with step(f"PUT {base_url_api}"):
        response = put_request(url='oauth2/access_token/')
        body = response.json()
        assert 'error' in body
        assert 'message' in body['error'] and 'Неверно передан параметр code' in body['error']['message']
        assert response.status_code == 401


@allure.epic('API')
@allure.label("owner", "Unauthorized key and login")
@allure.feature("Checking notexist method on the site")
@allure.tag('ui', 'api')
@allure.severity('normal')
@allure.label('layer', 'api')
def test_unblock_company():
    id = 1000000
    with step(f"DELETE {base_url_api}"):
        response = delete_request(url=f'clients/{id}/block/')
        body = response.json()
        assert response.status_code != 200
        assert 'error' in body
        assert 'message' in body['error'] and 'Неправильно набран адрес, или такой страницы "2.0/clients/1000000/block" на сайте больше не существует' in body['error']['message']