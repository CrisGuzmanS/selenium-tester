from abc import ABC, abstractmethod
import shared
from selenium.webdriver.common.by import By

class Findable(ABC):

    @abstractmethod
    def where_xpath(self, xpath:str):
        pass
        # return shared.element_finder.ElementFinder( (By.XPATH, xpath), self.driver )

    @abstractmethod
    def where_id(self, id:str):
        pass
        # return shared.element_finder.ElementFinder( (By.ID, id), self.driver )

    @abstractmethod
    def where_name(self, name:str):
        pass
        # return shared.element_finder.ElementFinder( (By.NAME, name), self.driver )

    @abstractmethod
    def where_contain_text(self, text:str):
        pass
        # return shared.element_finder.ElementFinder.where_xpath( f"//*[contains(text(), '{text}')]", self.driver )

    @abstractmethod
    def where_class_name(self, name:str):
        pass
        # return shared.element_finder.ElementFinder( (By.CLASS_NAME, name), self.driver )

    @abstractmethod
    def where_tag_name(self, name:str):
        pass