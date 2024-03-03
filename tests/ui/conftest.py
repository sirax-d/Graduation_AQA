import os

import pytest
from dotenv import load_dotenv
from selene import browser

load_dotenv()
base_url = os.getenv("BASE_URL")


@pytest.mark.login_cookie(reason="Login with cookie")
@pytest.fixture(scope='function', autouse=True)
def setup_browser_with_cookie_login():
    browser.config.base_url = base_url
    browser.config.window_width = '1200'
    browser.config.window_height = '1450'
    yield browser
    browser.quit()
