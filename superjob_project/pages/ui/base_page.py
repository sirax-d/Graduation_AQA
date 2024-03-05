import os

import pytest
from dotenv import load_dotenv
from selene import browser, be, have
from selene.support.shared.jquery_style import s, ss

from superjob_project.data.ui.users import person, employment, time_work

load_dotenv()
email = os.getenv("EMAIL")
phone = os.getenv("MOBILE_NUMBER")


class BasePage:
    def open(self):
        browser.open("")

    def registration(self):
        s("._38FKN.f-test-link-Registraciya").click()
        s(".f-test-link-Ya_ischu_rabotu_Hochu_razmestit_rezyume_i_otklikatsya_na_vakansii_luchshih_kompanij").click()
        s('[name="person.firstName"]').type(person.first_name)
        s('[name="person.lastName"]').type(person.last_name)
        ss('.f-test-input-birthDate')[1].type(person.birth_date)
        s('[name="phone"]').type(phone)
        s('[name="contacts.email"]').type(email)
        s('[name="position"]').type(employment.position)
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
        s('.mOBfu').should(be.not_.present)
        if s('.f-test-formField-error').with_(timeout=1).matching(be.visible):
            pytest.skip('Мы уже зарегистрированы, тест пропущен')
        else:
            self.check_registration()

    def check_registration(self):
        browser.open("")
        s(".f-test-tooltip-Nastrojki_Vyjti").should(be.visible)

    def advertising(self):
        browser.open("")
        s(".f-test-link-Reklama_na_sajte").click()
        browser.switch_to_next_tab()

    def check_advertising(self):
        s(".t-animate_started").should(be.visible)

    def change_type(self):
        s(".f-test-select-selected").click()
        ss("._6fVtm")[2].click()

    def check_change_type(self):
        s(".f-test-select-selected").should(have.text("Резюме"))

    def region_search(self):
        s("._3fBtg").click()
        s(".f-test-button-Ochistit").click()
        s(".f-test-input-geo").type("Санкт-Петербург")
        s(".f-test-checkable-Sankt-Peterburg").click()
        s(".f-test-button-Primenit").click()

    def check_region_search(self):
        s("._3fBtg").with_(timeout=3).should(have.text("Санкт-Петербург"))


base = BasePage()
