from superjob_project.pages.ui.base_page import base
import allure


@allure.epic('Unauthorized')
@allure.label("owner", "Without autohrized user")
@allure.feature("Checking advertising on the site")
@allure.tag('ui', 'normal')
@allure.severity('normal')
@allure.label('layer', 'ui')
def test_follow_links():
    with allure.step('Check advertising'):
        base.advertising()


@allure.epic('Unauthorized')
@allure.label("owner", "Without autohrized user")
@allure.feature("Checking type search")
@allure.tag('ui', 'normal')
@allure.severity('normal')
@allure.label('layer', 'ui')
def test_change_type():
    with allure.step('Change type'):
        base.change_type()

@allure.epic('Unauthorized')
@allure.label("owner", "Without autohrized user")
@allure.feature("Checking region search on the site")
@allure.tag('ui', 'normal')
@allure.severity('normal')
@allure.label('layer', 'ui')
def test_region_search():
    with allure.step('Region search'):
        base.region_search()
