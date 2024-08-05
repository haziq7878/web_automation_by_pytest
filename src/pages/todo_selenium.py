from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from src.pages.basePage import BasePageSelenium
from src.types.type import Options


class TodoPageSelenium(BasePageSelenium):
    CONTAINER: str = ".container"
    TODO_INPUT_OPTIONS = "li[ng-repeat*='sampletodo'] > input"
    FORM = "form[ng-submit]"

    def goto(self) -> "TodoPageSelenium":
        self.driver.get("https://lambdatest.github.io/sample-todo-app")
        return self

    def get_todo_by_name(self, name: Options) -> WebElement:
        parent_element: WebElement = self.UNIQUE_ELEMENT().find_element(
            By.XPATH, f"//span[text()='{name.value}']/preceding-sibling::input").parent
        return parent_element.find_element(By.CSS_SELECTOR, "input")
