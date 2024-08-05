from pylenium.driver import Pylenium, Element
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    UNIQUE_ELEMENT_SELECTOR: str

    def __init__(self, py: Pylenium, selector: str) -> None:
        self.py = py
        self.UNIQUE_ELEMENT_SELECTOR = selector

    def UNIQUE_ELEMENT(self) -> Element:
        return self.py.get(self.UNIQUE_ELEMENT_SELECTOR)


class BasePageSelenium:
    UNIQUE_ELEMENT_SELECTOR: str

    def __init__(self, driver: WebDriver, selector: str) -> None:
        self.driver = driver
        self.UNIQUE_ELEMENT_SELECTOR = selector

    def UNIQUE_ELEMENT(self) -> WebElement:
        return self.driver.find_element(By.CSS_SELECTOR, self.UNIQUE_ELEMENT_SELECTOR)
