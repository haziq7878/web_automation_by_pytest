from src.pages.basePage import BasePage


class FormComponent(BasePage):
    INPUT_FIELD = "#sampletodotext"
    ADD_BUTTON = "#addbutton"

    def submit(self) -> "FormComponent":
        self.py.get(self.ADD_BUTTON).click()
        return self

    def type_name_for_todo(self, name: str) -> None:
        self.py.get(self.INPUT_FIELD).type(name)
        return self

    def add_todo(self, name: str) -> "FormComponent":
        self.type_name_for_todo(name)
        return self.submit()
