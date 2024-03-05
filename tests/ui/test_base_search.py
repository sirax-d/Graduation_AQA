import allure

from superjob_project.pages.ui.base_page import base


@allure.epic('Unauthorized')
@allure.label("owner", "Without autohrized user")
@allure.feature("Checking advertising on the site")
@allure.tag('ui', 'normal')
@allure.severity('normal')
@allure.label('layer', 'ui')
def test_follow_links():
    with allure.step('Preparing for the test'):
        base.open()
    with allure.step('Check advertising'):
        base.advertising()
    with allure.step('Check links'):
        base.check_advertising()


@allure.epic('Unauthorized')
@allure.label("owner", "Without autohrized user")
@allure.feature("Checking type search")
@allure.tag('ui', 'normal')
@allure.severity('normal')
@allure.label('layer', 'ui')
def test_change_type():
    with allure.step('Preparing for the test'):
        base.open()
    with allure.step('Change type'):
        base.change_type()
    with allure.step('Check "change type"'):
        base.check_change_type()


@allure.epic('Unauthorized')
@allure.label("owner", "Without autohrized user")
@allure.feature("Checking region search on the site")
@allure.tag('ui', 'normal')
@allure.severity('normal')
@allure.label('layer', 'ui')
def test_region_search():
    with allure.step('Preparing for the test'):
        base.open()
    with allure.step('Region search'):
        base.region_search()
    with allure.step('Check "region search"'):
        base.check_region_search()
