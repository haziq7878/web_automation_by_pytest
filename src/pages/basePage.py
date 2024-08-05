from pylenium.driver import Pylenium, Element


class BasePage:
    UNIQUE_ELEMENT_SELECTOR: str

    def __init__(self, py: Pylenium, selector: str) -> None:
        self.py = py
        self.UNIQUE_ELEMENT_SELECTOR = selector

    def UNIQUE_ELEMENT(self) -> Element:
        return self.py.get(self.UNIQUE_ELEMENT_SELECTOR)
