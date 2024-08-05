from selenium.webdriver.common.by import By
from src.types.type import Options


def test_google_selenium(driver):
    driver.get("https://google.com")
    driver.find_element(by=By.CSS_SELECTOR, value="[name='q']").send_keys("puppies")
    driver.find_element(By.CSS_SELECTOR, "div.FPdoLc.lJ9FBc input.gNO89b").click()
    assert "puppies" in driver.title


def test_check_first_item(page_selenium):
    checkbox = page_selenium.get_todo_by_name(Options.FIFTH_ITEM)
    checkbox.click()
    assert checkbox.is_selected() is True
