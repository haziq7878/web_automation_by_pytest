import pytest
from pylenium.driver import Pylenium
from src.pages.todo import TodoPage


@pytest.fixture
def page(py: Pylenium):
    return TodoPage(py, ".container").goto()
