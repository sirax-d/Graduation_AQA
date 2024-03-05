import allure

from superjob_project.pages.ui.base_page import base


@allure.epic('Unauthorized')
@allure.label("owner", "Without autohrized user")
@allure.feature("Checking advertising on the site")
@allure.tag('ui', 'normal')
@allure.severity('normal')
@allure.label('layer', 'ui')
def test_follow_links():
    base.open()
    base.advertising()
    base.check_advertising()


@allure.epic('Unauthorized')
@allure.label("owner", "Without autohrized user")
@allure.feature("Checking type search")
@allure.tag('ui', 'normal')
@allure.severity('normal')
@allure.label('layer', 'ui')
def test_change_type():
    base.open()
    base.change_type()
    base.check_change_type()


@allure.epic('Unauthorized')
@allure.label("owner", "Without autohrized user")
@allure.feature("Checking region search on the site")
@allure.tag('ui', 'normal')
@allure.severity('normal')
@allure.label('layer', 'ui')
def test_region_search():
    base.open()
    base.region_search()
    base.check_region_search()
