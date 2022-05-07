from __future__ import annotations
import shared
from typing import TYPE_CHECKING
from selenium.webdriver.common.by import By

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.webdriver import WebDriver

class Element():
    """A class that represents a DOM element

    """

    def __init__(self, element: WebElement, driver: WebDriver):
        """

        Args:
            element (WebElement): web element to wrap
            driver (WebDriver): web driver
        """

        self.driver = driver
        self.element = element

    def type(self, text:str):
        """
        Types an specific text in an input field

        """

        self.element.send_keys(text)

    def text(self) -> str:
        """gets the inner text of the element

        Returns:
            str: inner text of the element
        """

        return self.element.text

    def html(self) -> str:
        """gets the inner html of the element

        Returns:
            str: the inner html of the element
        """

        return self.element.get_attribute('innerHTML')

    def attribute(self, name:str) -> str:
        """gets the attribute's value

        Args:
            name (str): name of the attribute to search

        Returns:
            str: attribute's value
        """

        return self.element.get_attribute(name)

    def click(self):
        """clicks the element

        """
        self.element.click()

    def clear(self):
        """clear the input field

        """

        self.element.clear()

    def children(self) -> shared.element_collection.ElementCollection:
        """gets a collection of the next children elements

        Returns:
            ElementCollection
        """
        return shared.element_collection.ElementCollection(
            self.element.find_elements(By.XPATH,"./child::*"),
            self.driver
        )

    def where_tag_name(self, name:str) -> shared.element_finder.ElementFinder:
        """find a subelement with the tag name specified

        Args:
            name (str): name of the tag to search

        Returns:
            ElementFinder
        """

        return shared.element_finder.ElementFinder.where_tag_name(
            name,
            self.driver,
            self.element
        )

    def where_attribute(self, attribute:str, value:str) -> shared.element_finder.ElementFinder:
        """find a subelement with the attribute and value specified

        Args:
            attribute (str): the attribute of the element
            value (str): the value of the attribute

        Returns:
            shared.element_finder.ElementFinder
        """

        return shared.element_finder.ElementFinder.where_xpath(
            f".//*[@{attribute}='{value}']",
            self.driver,
            self.element
        )