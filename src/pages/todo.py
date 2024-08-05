from enum import Enum
from pylenium.driver import Element, Elements
from src.pages.basePage import BasePage
from src.pages.form import FormComponent


class Options(Enum):
    FIRST_ITEM = "First Item"
    SECOND_ITEM = "Second Item"
    THIRD_ITEM = "Third Item"
    FORTH_ITEM = "Fourth Item"
    FIFTH_ITEM = "Fifth Item"


class TodoPage(BasePage):
    CONTAINER: str = ".container"
    TODO_INPUT_OPTIONS = "li[ng-repeat*='sampletodo'] > input"
    FORM = "form[ng-submit]"

    def goto(self) -> "TodoPage":
        self.py.visit("https://lambdatest.github.io/sample-todo-app")
        return self

    def get_todo_by_name(self, name: Options) -> Element:
        parent_element = self.UNIQUE_ELEMENT().getx(
            f"//span[text()='{name.value}']/preceding-sibling::input").parent()
        return parent_element.get("input")

    def get_all_todos(self) -> Elements:
        return self.UNIQUE_ELEMENT().find(self.TODO_INPUT_OPTIONS)

    def get_submit_form(self) -> "FormComponent":
        return FormComponent(self.py, self.FORM)
