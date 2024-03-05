from appium.webdriver.common.appiumby import AppiumBy
from selene import have, be
from selene.support.shared.jquery_style import s, ss


class BasePage:

    def info(self):
        s((AppiumBy.ID, 'ru.superjob.client.android:id/closeButton')).click()
        s((AppiumBy.ID, 'ru.superjob.client.android:id/actionMore')).click()
        s((AppiumBy.XPATH, '//android.widget.TextView[@text="О компании"]')).click()

    def company_info_check(self):
        s((AppiumBy.XPATH,
           '//android.widget.TextView[@resource-id="ru.superjob.client.android:id/companyHeaderDescription"]')) \
            .should(have.text('Клиент SuperJob с 2000 года'))

    def response(self):
        s((AppiumBy.ID, 'ru.superjob.client.android:id/closeButton')).click()
        s((AppiumBy.ID, 'ru.superjob.client.android:id/actionResponses')).click()

    def response_check(self):
        s((AppiumBy.CLASS_NAME, 'android.widget.TextView')).should(have.text('Здесь будут ваши отклики'))
        s((AppiumBy.XPATH,
           '//android.widget.ScrollView/android.view.View/android.view.View/android.widget.Button')).matching(
            be.visible)

    def find_vacancy_without_login(self):
        s((AppiumBy.ID, 'ru.superjob.client.android:id/closeButton')).click()
        s((AppiumBy.XPATH, '//android.widget.TextView[@text="Поиск работы"]')).click()
        s((AppiumBy.CLASS_NAME, 'android.widget.EditText')).type('Python')
        ss((AppiumBy.CLASS_NAME, 'android.widget.TextView'))[1].click()

    def check_results_vacancy(self):
        s((AppiumBy.CLASS_NAME, 'android.widget.TextView')).should(have.text('ВАКАНСИЙ'))


base_page = BasePage()
