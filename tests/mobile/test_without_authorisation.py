import allure
import pytest

from superjob_project.pages.mobile.base_page import base_page


@allure.epic('Unauthorized')
@allure.label("owner", "Without autohrized user")
@allure.feature("Checking search vacancy without login")
@allure.tag('mobile', 'normal')
@allure.severity('normal')
@allure.label('layer', 'mobile')
def test_search_vacancy():
    with allure.step('Ищем вакансию без авторизации'):
        base_page.sj_find_vacancy_without_login()
    with allure.step('Проверяем результаты поиска'):
        base_page.check_results_vacancy()


@allure.epic('Unauthorized')
@allure.label("owner", "Without autohrized user")
@allure.feature("Checking information about the company without login")
@allure.tag('mobile', 'normal')
@allure.severity('normal')
@allure.label('layer', 'mobile')
def test_company_info():
    with allure.step('Переходим в информацию о компании SJ без авторизации'):
        base_page.sj_info()
    with allure.step('Проверяем наличие информации о компании'):
        base_page.sj_company_info_check()


@allure.epic('Unauthorized')
@allure.label("owner", "Without autohrized user")
@allure.feature("Checking menu responses without login")
@allure.tag('mobile', 'normal')
@allure.severity('normal')
@allure.label('layer', 'mobile')
@pytest.mark.mobile
def test_response_menu():
    with allure.step('Переходим в  меню откликов неавторизованным пользователем'):
        base_page.sj_response()
    with allure.step('Проверяем наличие информации в меню откликов'):
        base_page.sj_response_check()
