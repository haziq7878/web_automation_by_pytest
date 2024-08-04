from enum import Enum
import pytest
from pylenium.driver import Pylenium, Element, Elements


class Options(Enum):
    FIRST_ITEM = "First Item"
    SECOND_ITEM = "Second Item"
    THIRD_ITEM = "Third Item"
    FORTH_ITEM = "Fourth Item"
    FIFTH_ITEM = "Fifth Item"


class TodoPage:
    def __init__(self, py: Pylenium) -> None:
        self.py = py

    def goto(self) -> "TodoPage":
        self.py.visit("https://lambdatest.github.io/sample-todo-app")
        return self

    def get_todo_by_name(self, name: Options) -> Element:
        return self.py.getx(f"//span[text()='{name.value}']/preceding-sibling::input")

    def get_all_todos(self) -> Elements:
        return self.py.find("li[ng-repeat*='sampletodo']")


@pytest.fixture
def page(py: Pylenium):
    return TodoPage(py).goto()
