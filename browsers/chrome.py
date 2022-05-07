from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

class ChromeBrowser:
    
    def __init__(self):
        s = Service('/usr/bin/chromedriver')
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--incognito')
        self._driver = webdriver.Chrome(service=s, options=options)
        self._driver.set_window_size(1400,1000)
        self._driver.delete_all_cookies()

    def chrome_driver(self):
        return self._driver