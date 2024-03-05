import allure

from superjob_project.pages.mobile.auth_page import account_page


@allure.epic('authorized')
@allure.label("owner", "With autohrized user")
@allure.feature("Checking mobile login")
@allure.tag('mobile', 'normal')
@allure.severity('normal')
@allure.label('layer', 'mobile')
def test_login_mobile():
    with allure.step('Логинимся'):
        account_page.login()
    with allure.step('Проверяем успешный логин'):
        account_page.check()


@allure.epic('authorized')
@allure.label("owner", "With autohrized user")
@allure.feature("Checking search vacancy with login")
@allure.tag('mobile', 'normal')
@allure.severity('normal')
@allure.label('layer', 'mobile')
def test_search_with_login():
    with allure.step('Логинимся'):
        account_page.login()
    with allure.step('Ищем вакансию авторизованным пользователем'):
        account_page.find_vacancy_login()
    with allure.step('Проверяем результаты поиска'):
        account_page.check_results_vacancy()
