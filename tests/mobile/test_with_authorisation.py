import allure
import pytest

from superjob_project.pages.mobile.auth_page import account_page


@allure.epic('authorized')
@allure.label("owner", "With autohrized user")
@allure.feature("Checking mobile login")
@allure.tag('mobile', 'normal')
@allure.severity('normal')
@allure.label('layer', 'mobile')
@pytest.mark.mobile
def test_login_mobile():
    with allure.step('Логинимся'):
        account_page.sj_mobile_login()
    with allure.step('Проверяем успешный логин'):
        account_page.sj_login_check()


@allure.epic('authorized')
@allure.label("owner", "With autohrized user")
@allure.feature("Checking search vacancy with login")
@allure.tag('mobile', 'normal')
@allure.severity('normal')
@allure.label('layer', 'mobile')
@pytest.mark.mobile
def test_search_with_login():
    with allure.step('Логинимся'):
        account_page.sj_mobile_login()
    with allure.step('Ищем вакансию авторизованным пользователем'):
        account_page.sj_find_vacancy_login()
    with allure.step('Проверяем результаты поиска'):
        account_page.check_results_vacancy()
