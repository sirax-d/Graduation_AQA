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
    with allure.step('Preconditions: open SJ site'):
        base.open()
    with allure.step('Create account and check successful registration depending of "if"'):
        base.registration()


@allure.epic('Authorized')
@allure.label("owner", "Autohrized user")
@allure.feature("Checking the authorization user and response to the vacancy")
@allure.tag('ui', 'normal')
@allure.severity('normal')
@allure.label('layer', 'ui')
@pytest.mark.xfail(reason="Нестабильный тест")
def test_login_and_response():
    with allure.step('Preconditions: open SJ site'):
        base.open()
    with allure.step('Login in SJ site and create response to the vacancy'):
        account.login()
        account.create_response()
    with allure.step('Check response'):
        account.check_response()


@allure.epic('Authorized')
@allure.label("owner", "Autohrized user")
@allure.feature("Checking the authorization user and create resume")
@allure.tag('ui', 'normal')
@allure.severity('normal')
@allure.label('layer', 'ui')
@pytest.mark.xfail(reason="Нестабильный тест, динамические окна")
def test_create_resume():
    with allure.step('Preconditions: open SJ site'):
        base.open()
    with allure.step('Login in SJ site and create resume'):
        account.login()
        account.create_resume()
    with allure.step('Check create resume'):
        account.check_create_resume()


@allure.epic('Authorized')
@allure.label("owner", "Autohrized user")
@allure.feature("Checking the authorization user and close visibility of the resume")
@allure.tag('ui', 'normal')
@allure.severity('normal')
@allure.label('layer', 'ui')
def test_resume_visibility_off():
    with allure.step('Preconditions: open SJ site'):
        base.open()
    with allure.step('Login in SJ site'):
        account.login()
    with allure.step('Create other resume, and close visibility")'):
        account.create_other_resume()
    with allure.step('Check visibility of the resume'):
        account.check_visibility()


@allure.epic('Authorized')
@allure.label("owner", "Autohrized user")
@allure.feature("Checking base authorization user")
@allure.tag('ui', 'normal')
@allure.severity('normal')
@allure.label('layer', 'ui')
def test_auth():
    with allure.step('Preconditions: open SJ site'):
        base.open()
    with allure.step('Login in SJ site'):
        account.login()
    with allure.step('Check successful login'):
        account.check_login()


@allure.epic('Authorized')
@allure.label("owner", "Autohrized user")
@allure.feature("Checking base authorization user and logout")
@allure.tag('ui', 'normal')
@allure.severity('normal')
@allure.label('layer', 'ui')
def test_logout():
    with allure.step('Preconditions: open SJ site'):
        base.open()
    with allure.step('Login and logout in SJ site'):
        account.login()
        account.logout()
    with allure.step('Check logout'):
        account.check_logout()
