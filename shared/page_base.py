from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from exceptions.element_not_found_exception import ElementNotFoundException
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime
from shared.findable import Findable
from shared.element_finder import ElementFinder
from selenium.webdriver.common.by import By

class PageBase(Findable):

    def __init__(self, driver):
        self.driver = driver

    def webdriver(self):
        return self.driver

    def screenshot(self, name:str):
        self.driver.get_screenshot_as_file(f"images/{name}")

    def snapshot(self):
        self.screenshot(f"{datetime.now().strftime('%d-%m-%Y-%H-%M-%S')}.png")

    def wait(self, seconds:int):
        self.driver.implicitly_wait(seconds)

    def visit(self, url:str) -> None:
        self.driver.get(url)

    def where_xpath(self, xpath:str) -> ElementFinder:
        return ElementFinder(
            locator = (By.XPATH, xpath),
            driver = self.driver
        )

    def where_id(self, id:str) -> ElementFinder:
        return ElementFinder(
            (By.ID, id),
            self.driver
        )

    def where_name(self, name:str) -> ElementFinder:
        return ElementFinder(
            (By.NAME, name),
            self.driver
        )

    def where_contain_text(self, text:str) -> ElementFinder:
        return ElementFinder.where_xpath(
            f"//*[contains(text(), '{text}')]",
            self.driver
        )

    def where_class_name(self, name:str) -> ElementFinder:
        return ElementFinder(
            (By.CLASS_NAME, name),
            self.driver
        )

    def where_tag_name(self, name:str) -> ElementFinder:
        return ElementFinder(
            (By.TAG_NAME, name),
            self.driver
        )

    def where_attribute(self, attribute, value) -> ElementFinder:
        return ElementFinder(
            (By.XPATH, f"//*[@{attribute}='{value}']"),
            self.driver
        )