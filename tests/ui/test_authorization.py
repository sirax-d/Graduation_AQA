import allure
import pytest

from superjob_project.pages.ui.account_page import account
from superjob_project.pages.ui.base_page import base


@allure.epic('Authorized')
@allure.label("owner", "Autohrized user")
@allure.feature("Checking the authorization of the user")
@allure.tag('ui', 'normal')
@allure.severity('normal')
@allure.label('layer', 'ui')
def test_create_account():
    base.open()
    base.registration()


@allure.epic('Authorized')
@allure.label("owner", "Autohrized user")
@allure.feature("Checking the authorization user and response to the vacancy")
@allure.tag('ui', 'normal')
@allure.severity('normal')
@allure.label('layer', 'ui')
@pytest.mark.xfail(reason="Нестабильный тест")
def test_login_and_response():
    base.open()
    account.login()
    account.create_response()
    account.check_response()


@allure.epic('Authorized')
@allure.label("owner", "Autohrized user")
@allure.feature("Checking the authorization user and create resume")
@allure.tag('ui', 'normal')
@allure.severity('normal')
@allure.label('layer', 'ui')
@pytest.mark.xfail(reason="Нестабильный тест, динамические окна")
def test_create_resume():
    base.open()
    account.login()
    account.create_resume()
    account.check_create_resume()


@allure.epic('Authorized')
@allure.label("owner", "Autohrized user")
@allure.feature("Checking the authorization user and close visibility of the resume")
@allure.tag('ui', 'normal')
@allure.severity('normal')
@allure.label('layer', 'ui')
def test_resume_visibility_off():
    base.open()
    account.login()
    account.create_other_resume()
    account.check_visibility()


@allure.epic('Authorized')
@allure.label("owner", "Autohrized user")
@allure.feature("Checking base authorization user")
@allure.tag('ui', 'normal')
@allure.severity('normal')
@allure.label('layer', 'ui')
def test_auth():
    base.open()
    account.login()
    account.check_login()


@allure.epic('Authorized')
@allure.label("owner", "Autohrized user")
@allure.feature("Checking base authorization user and logout")
@allure.tag('ui', 'normal')
@allure.severity('normal')
@allure.label('layer', 'ui')
def test_logout():
    base.open()
    account.login()
    account.logout()
    account.check_logout()
