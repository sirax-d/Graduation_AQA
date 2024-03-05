import allure

from superjob_project.pages.mobile.base_page import base_page


@allure.epic('Unauthorized')
@allure.label("owner", "Without autohrized user")
@allure.feature("Checking search vacancy without login")
@allure.tag('mobile', 'normal')
@allure.severity('normal')
@allure.label('layer', 'mobile')
def test_search_vacancy():
    base_page.find_vacancy_without_login()
    base_page.check_results_vacancy()


@allure.epic('Unauthorized')
@allure.label("owner", "Without autohrized user")
@allure.feature("Checking information about the company without login")
@allure.tag('mobile', 'normal')
@allure.severity('normal')
@allure.label('layer', 'mobile')
def test_company_info():
    base_page.info()
    base_page.company_info_check()


@allure.epic('Unauthorized')
@allure.label("owner", "Without autohrized user")
@allure.feature("Checking menu responses without login")
@allure.tag('mobile', 'normal')
@allure.severity('normal')
@allure.label('layer', 'mobile')
def test_response_menu():
    base_page.response()
    base_page.response_check()
