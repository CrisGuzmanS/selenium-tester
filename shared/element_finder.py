from .element_collection import ElementCollection

from .element import Element
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from exceptions.element_not_found_exception import ElementNotFoundException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class ElementFinder:

    def __init__(self, locator: dict, driver, element=None):
        self.locator = locator
        self.driver = driver
        self.element = element
        self.wait = 0

    def until(self, seconds):
        self.wait = seconds
        return self

    def get(self):
        try:

            scope = self.element if self.element else self.driver

            return ElementCollection(
                WebDriverWait(scope, self.wait).until(
                    EC.presence_of_all_elements_located(self.locator)
                ),
                self.driver
            )
        except TimeoutException:
            self.driver.get_screenshot_as_file( "images/errors/"+datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f).png") )
            raise ElementNotFoundException(f"el elemento ({','.join(self.locator)}) no fue encontrado")

    def first(self):
        try:

            scope = self.element if self.element else self.driver

            return Element(
                WebDriverWait(scope, self.wait).until(
                    EC.element_to_be_clickable(self.locator)
                ),
                self.driver
            )
        except TimeoutException:
            self.driver.get_screenshot_as_file( "images/errors/"+datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f).png") )
            raise ElementNotFoundException(f"el elemento ({','.join(self.locator)}) no fue encontrado")

    @staticmethod
    def where_xpath(xpath:str, driver, element=None):
        return ElementFinder( (By.XPATH, xpath), driver , element)

    @staticmethod
    def where_id(id:str, driver, element=None):
        return ElementFinder( (By.ID, id), driver, element)

    @staticmethod
    def where_name(name:str, driver, element=None):
        return ElementFinder( (By.NAME, name), driver , element)

    @staticmethod
    def where_contain_text(text:str, driver, element=None):
        return ElementFinder.where_xpath( f"//*[contains(text(), '{text}')]", driver , element)

    def where_class_name(name:str, driver, element=None):
        return ElementFinder( (By.CLASS_NAME, name), driver , element)

    @staticmethod
    def where_tag_name(name:str, driver, element=None):
        return ElementFinder( (By.TAG_NAME, name), driver, element )