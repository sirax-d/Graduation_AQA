import os

import allure
from allure_commons._allure import step
from dotenv import load_dotenv
from jsonschema import validate

from superjob_project.data.api.schemas import post_vacancy_forgot_password_schema
from superjob_project.utils.base_requests import post_request

load_dotenv()
base_url_api = os.getenv("BASE_URL_API")
email = os.getenv("EMAIL")


@allure.epic('API')
@allure.label("owner", "Without authorize key")
@allure.feature("Checking function forgot password on the site")
@allure.tag('ui', 'api')
@allure.severity('normal')
@allure.label('layer', 'api')
def test_post_password_reset():
    with step(f"POST {base_url_api}"):
        response = post_request(url='forgot_password/')
        body = response.json()
        validate(body, post_vacancy_forgot_password_schema)
        assert body['result'] == True
