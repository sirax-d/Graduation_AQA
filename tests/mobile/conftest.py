import allure
import allure_commons
import pytest
from appium import webdriver
from dotenv import load_dotenv
from selene import browser, support

from superjob_project.utils.attach import add_screenshot, add_xml, attach_bstack_video


def pytest_addoption(parser):
    parser.addoption(
        "--context",
        required=False,
        default="bs",
        choices=['local', 'bs'],
    )


def pytest_configure(config):
    context = config.getoption("--context")
    load_dotenv(dotenv_path=f'.env.{context}')


@pytest.fixture
def context(request):
    return request.config.getoption("--context")


@pytest.fixture(scope='function', autouse=True)
def android_mobile_management(context):
    from config import config

    options = config.to_driver_options(context=context)

    with allure.step('setup app session'):
        browser.config.driver = webdriver.Remote(
            options.get_capability('remote_url'),
            options=options
        )

    browser.config.timeout = 15.0

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext)

    yield

    add_screenshot(browser)

    add_xml(browser)

    if context == 'bs':
        session_id = browser.driver.session_id

        with allure.step('tear down app session with id' + session_id):
            browser.quit()

        bstack = options.get_capability('bstack:options')
        login = bstack['userName']
        password = bstack['accessKey']
        attach_bstack_video(session_id, login, password)

    browser.quit()
