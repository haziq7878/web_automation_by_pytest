from src.pages.todo import TodoPage, Options


def test_check_first_item(page: TodoPage):
    checkbox = page.get_todo_by_name(Options.FIFTH_ITEM)
    checkbox.click()
    assert checkbox.should().be_checked()


def test_check_many_item(page: TodoPage):
    todos = page.get_all_todos()
    todo2, todo4 = todos[1], todos[3]
    todo2.click()
    todo4.click()
    assert page.py.contains("3 of 5 remaining")


def test_check_all_remaining(page: TodoPage):
    for todo in page.get_all_todos():
        todo.click()

    assert page.py.contains("0 of 5 remaining")


def test_add_new_item(page: TodoPage):
    form = page.get_submit_form()
    form.add_todo("Finish the course")
    assert page.get_all_todos().should().have_length(6)
    assert page.py.contains("6 of 6 remaining")
