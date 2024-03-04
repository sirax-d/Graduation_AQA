import os

from appium.webdriver.common.appiumby import AppiumBy
from dotenv import load_dotenv
from selene import have, be
from selene.support.shared.jquery_style import s, ss

load_dotenv()
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")


class SuperJobAccountPage:
    def sj_mobile_login(self):
        s((AppiumBy.ID, 'ru.superjob.client.android:id/closeButton')).click()
        s((AppiumBy.XPATH, '//android.view.View[@content-desc="Вход"]')).click()
        s((AppiumBy.XPATH, '//android.widget.EditText[@resource-id="Телефон или email"]')).type(email)
        s((AppiumBy.XPATH, '//android.widget.ScrollView/android.view.View[1]/android.widget.Button')).click()
        s((AppiumBy.XPATH, '//android.widget.EditText[@resource-id="Пароль"]')).type(password)
        s((AppiumBy.XPATH,
           '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.widget.Button')).click()

    def sj_login_check(self):
        s((AppiumBy.ID, 'ru.superjob.client.android:id/vbwiPrimaryButton')).should(be.not_.visible)

    def sj_find_vacancy_login(self):
        s((AppiumBy.XPATH, '//android.widget.TextView[@text="Поиск работы"]')).click()
        s((AppiumBy.CLASS_NAME, 'android.widget.EditText')).type('Python').with_(timeout=30)
        ss((AppiumBy.CLASS_NAME, 'android.widget.TextView'))[1].click()

    def check_results_vacancy(self):
        s((AppiumBy.CLASS_NAME, 'android.widget.TextView')).should(have.text('ВАКАНСИЙ'))


account_page = SuperJobAccountPage()
