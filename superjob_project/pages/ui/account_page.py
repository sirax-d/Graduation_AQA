import os

from dotenv import load_dotenv
from selene import browser, be, have
from selene.support.shared.jquery_style import s, ss

from superjob_project.data.ui.users import person, employment, time_work

load_dotenv()
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")


class AccountPage:
    def open(self):
        browser.open("")

    def create_resume(self):
        browser.open("user/resume/")
        if s('.f-test-button-Vsjo_verno').matching(be.visible):
            s('.f-test-button-Vsjo_verno').click()
        s(".f-test-button-Sozdat_rezyume").should(be.clickable).click()
        s('[name="person.firstName"]').clear().type(person.first_name)
        s('[name="person.lastName"]').clear().type(person.last_name)
        s('[name="position"]').type('Other' + employment.position)
        s('[name="salary"]').type(employment.salary)
        s('[name="experience.position"]').type(employment.experience)
        s('[name="resumeCompany.title"]').type(employment.company_title)
        s('[name="resumeCompany.description"]').type(employment.company_description)
        s('[name="month"]').set_value(time_work.month)
        s('[name="year"]').type(time_work.year)
        ss('.f-test-input-month')[1].type(time_work.month_end)
        ss('.f-test-input-year')[1].type(time_work.year_end)
        s('[name="responsibility"]').type(employment.work_description)
        s(".f-test-button-Sohranit").click()
        s(".f-test-button-Sohranit").click()


    def check_create_resume(self):
        s("._2yXpl._2d-4z.I16fU._3bSIo").should(have.text("Отлично! Резюме опубликовано"))

    def create_response(self):
        browser.open('vakansii/inzhener-47454519.html')
        if s('.f-test-button-Vsjo_verno').matching(be.visible):
            s('.f-test-button-Vsjo_verno').click()
        s('.f-test-button-Otkliknutsya').click()
        s('.f-test-button-Otkliknutsya').click()
        s('.f-test-button-close').click()

    def close_visibility(self):
        browser.open("user/resume/")
        if s('.f-test-button-Vsjo_verno').matching(be.visible):
            s('.f-test-button-Vsjo_verno').click()
        ss(".f-test-clickable-Izmenit")[0].click()
        s(".f-test-switcher-button-Dostup_k_rezyume_zakryt").click()
        s(".f-test-button-Sohranit").click()

    def check_visibility(self):
        browser.open("user/resume/")
        s(".f-test-resume_card").should(have.text("Доступ к резюме закрыт"))

    def check_response(self):
        browser.open("user/responses/")
        s(".f-test-response-list").should(be.visible)

    def create_other_resume(self):
        if s('.f-test-button-Vsjo_verno').matching(be.visible):
            s('.f-test-button-Vsjo_verno').click()
        s(".f-test-button-dehaze").click()
        s(".f-test-link-Rezyume").double_click()
        s(".f-test-link-Sozdat_rezyume").click()
        s('[name="position"]').type("Mix developer")
        s('[name="salary"]').type("50000")
        s('[name="experience.position"]').type("2 automation QA")
        s('[name="resumeCompany.title"]').type("QA.GURU")
        s('[name="resumeCompany.description"]').type("Образование")
        s('[name="month"]').set_value("Январь")
        s('[name="year"]').type("2018")
        ss('.f-test-input-month')[1].type(time_work.month_end)
        ss('.f-test-input-year')[1].type(time_work.year_end)
        s('[name="responsibility"]').type("Изучал автоматизацию тестирования")
        s(".f-test-button-Sohranit").click()

    def login(self):
        if s('.f-test-button-Vsjo_verno').matching(be.visible):
            s('.f-test-button-Vsjo_verno').click()
        s("._38FKN.f-test-link-Vhod").click()
        s('[name="login"]').type(email)
        s('[name="password"]').type(password)
        s('.f-test-button-Vojti').with_(timeout=3).click()

    def check_login(self):
        s(".f-test-tooltip-Nastrojki_Vyjti").matching(be.visible)

    def logout(self):
        if s('.f-test-button-Vsjo_verno').matching(be.visible):
            s('.f-test-button-Vsjo_verno').click()
        s(".f-test-tooltip-Nastrojki_Vyjti").click()
        s(".f-test-button-Vyjti").click()

    def check_logout(self):
        s(".f-test-link-Vhod").should(be.visible)


account = AccountPage()
