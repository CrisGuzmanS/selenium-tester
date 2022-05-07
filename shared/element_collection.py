from __future__ import annotations
import random
from .element import Element
from selenium.webdriver.chrome.webdriver import WebDriver

class ElementCollection:

    def __init__(self, collection, driver:WebDriver):
        self._collection = collection
        self.driver = driver

    def get(self) -> list:
        return self._collection

    def first(self) -> Element:
        return Element(self._collection[0], self.driver)

    def find(self, index: int) -> Element:
        return Element(self._collection[index], self.driver)

    def random(self) -> Element:
        return Element( random.choice(self._collection), self.driver )

    def count(self) -> int:
        return len(self._collection)

    def map(self, function) -> list:
        new_collection = []

        for element in self._collection:
            new_collection.append( function( Element(element, self.driver) ) )

        return new_collection

    def filter(self, function) -> ElementCollection:
        
        new_collection = []

        for element in self._collection:
            if function( Element(element, self.driver) ):
                new_collection.append(element)

        return ElementCollection(new_collection, self.driver)

    def take(self, number:int) -> ElementCollection:
        return ElementCollection(self._collection[0:number], self.driver)

    def is_empty(self) -> bool:
        return False if len(self._collection) > 0 else True