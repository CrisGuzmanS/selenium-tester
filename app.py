from browsers.firefox import FirefoxBrowser
from browsers.chrome import ChromeBrowser

from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.evaluators_index_page import EvaluatorsIndexPage
from pages.evaluators_edit_page import EvaluatorsEditPage

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import time

class ProcienciaTest(unittest.TestCase):

    def setUp(self):
        self.driver = ChromeBrowser().chrome_driver()
        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.evaluators_index_page = EvaluatorsIndexPage(self.driver)
        self.evaluators_edit_page = EvaluatorsEditPage(self.driver)

    def test_user_admin_can_update_evaluator_details(self):
        self.login()
        self.go_to_evaluators_details()
        self.select_first_evaluator()
        self.open_edit_contact_details_modal()
        self.update_full_name()
        self.add_email("correo@selenium.com")
        self.update_addres("mi dirección")
        self.update_phone("5512328188")
        self.submit_contact_details()

    def submit_contact_details(self):
        self.evaluators_edit_page.update_concact_details_button().click()
        self.evaluators_edit_page.wait(5)
        self.evaluators_edit_page.snapshot()

    def update_phone(self, phone:str):
        self.evaluators_edit_page.phone_input().clear()
        self.evaluators_edit_page.phone_input().type(phone)

    def update_addres(self, address:str):
        self.evaluators_edit_page.address_textarea().clear()
        self.evaluators_edit_page.address_textarea().type(address)
        self.evaluators_edit_page.wait(3)
        self.evaluators_edit_page.snapshot()

    def add_email(self, mail:str):
        self.evaluators_edit_page.email_input().type(mail)

        self.evaluators_edit_page.add_email_input().click()

    def update_full_name(self):
        self.evaluators_edit_page.full_name_input().type("sasasa")

    def open_edit_contact_details_modal(self):
        self.evaluators_edit_page.edit_contact_details_button().click()
        self.evaluators_edit_page.snapshot()

    def select_first_evaluator(self):
        self.evaluators_index_page \
            .cards() \
            .first() \
            .where_attribute("data-original-title", "Actualizar información") \
            .first() \
            .click() \

    def go_to_evaluators_details(self):
        self.home_page.evaluators_section_button().click()

    def login(self):
        self.login_page.visit("http://192.168.1.203:8000/login")
        self.login_page.login_input().type("cguzman@ibsaweb.com")
        self.login_page.password_input().type("¡MyP4ssw0rd!")
        self.login_page.submit_button().click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()