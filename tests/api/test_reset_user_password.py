import os

import allure
from allure_commons._allure import step
from jsonschema import validate

from superjob_project.schemas.schemas import vacancy_forgot_password_schema
from superjob_project.utils.base_requests import post_request
from tests.api.conftest import base_url_api


@allure.epic('API')
@allure.label("owner", "Without access key")
@allure.feature("Checking function forgot password on the site")
@allure.tag('ui', 'api')
@allure.severity('normal')
@allure.label('layer', 'api')
def test_post_password_reset():
    with step(f"POST {base_url_api}"):
        response = post_request(url='forgot_password/')
        body = response.json()
        validate(body, vacancy_forgot_password_schema)
        assert body['result'] is True
        assert response.status_code == 200
