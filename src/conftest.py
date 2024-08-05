import os
import pytest
from pylenium.driver import Pylenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from src.pages.todo import TodoPage
from src.pages.todo_selenium import TodoPageSelenium


def pytest_addoption(parser):
    parser.addoption(
        "--remote", action="store", default="false",
        choices=["true", "false"], help="Run tests on LambdaTest (true/false)"
    )


@pytest.fixture
def pass_gen(request) -> dict[str, any]:
    """
    Fixture to accept the remote input from the command line.
    :param request: pytest request object

    :return: Tuple of length and number of alpha num characters
    """

    remote = request.config.getoption("--remote") == "true"

    data = {
        "remote": remote
    }

    return data


@pytest.fixture
def page(py: Pylenium):
    return TodoPage(py, ".container").goto()


@pytest.fixture
def page_selenium(driver):
    return TodoPageSelenium(driver, ".container").goto()


# This is for selenium connection to webdriver
# For pylenium check pylenium.json
@pytest.fixture
def driver(pass_gen):
    remote = pass_gen["remote"]
    if remote:

        # 1. Define username, access_key and remote url
        username = os.getenv("LT_USERNAME")
        access_key = os.getenv("LT_ACCESS_KEY")
        tunnel_id = os.getenv('TUNNEL', False)
        build = os.getenv('BUILD', "Sample PY Build")
        remote_url = f"https://{username}:{access_key}@hub.lambdatest.com/wd/hub"

        # 2. Define the desired capabilities for test run
        chrome_options = webdriver.ChromeOptions()
        chrome_options.set_capability("browserName", "Chrome")
        chrome_options.set_capability("browserVersion", "126")
        chrome_options.set_capability("platformName", "Windows 10")

        lt_options = {
            "username": username,
            "accessKey": access_key,
            "video": True,
            "platformName": "Windows 10",
            "build": build,
            "project": "testing",
            "tunnel": tunnel_id,
            "w3c": True,
            "plugin": "python-pytest"
        }
        chrome_options.set_capability("LT:Options", lt_options)

        driver = webdriver.Remote(command_executor=remote_url, options=chrome_options)
    else:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")  # Open Chrome in maximized mode
        chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
        chrome_options.add_argument("--no-sandbox")  # Disable sandbox for testing purposes

        # Path to the ChromeDriver executable
        # Update this to the location of your ChromeDriver
        chrome_driver_path = '/opt/homebrew/bin/chromedriver'

        # Create a new instance of the Chrome driver
        driver = webdriver.Chrome(service=ChromeService(
            executable_path=chrome_driver_path), options=chrome_options)

    yield driver

    driver.quit()
