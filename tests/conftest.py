import os.path
import platform

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from uitilites.Logger import setup_logging, Step
from uitilites.readProperties import getConfig


def pytest_addoption(parser):
    parser.addoption(
        "--browsername", action="store", default="chrome"
    )
    parser.addoption(
        "--headless", action="store_true", default=False
    )


@pytest.fixture(scope="session", autouse=True)
def Get_log():
    file = "./Log/logfile.log"
    if os.path.exists(file):
        os.remove(file)
    yield setup_logging(file)


url = getConfig().get('static data', 'url')
implicit_wait = float(getConfig().get('static data', 'implicit_wait'))


@pytest.fixture(scope="class", autouse=True)
def Setup_TearDown(request):
    global driver
    browser_name: [str] = request.config.getoption("--browsername")
    if browser_name.lower() == "chrome":
        driver = Chrome_Option(request)
    elif browser_name.lower() == "firefox":
        driver = Firefox_Option(request)
    elif browser_name.lower() == "edge":
        driver = Edge_Option(request)
    else:
        raise Exception("Browser not Present")
    allure.attach(f"Python Version :{platform.python_version()}", name="Python Version",
                  attachment_type=allure.attachment_type.TEXT)
    allure.attach(f"Platform Info :{platform.platform()}", name="Platform Info",
                  attachment_type=allure.attachment_type.TEXT)
    allure.attach(f"Browser Name :{driver.name}", name="Browser Name", attachment_type=allure.attachment_type.TEXT)
    driver.get(url)
    allure.attach(f"Url :{url}", name="Application url", attachment_type=allure.attachment_type.TEXT)
    driver.maximize_window()
    driver.implicitly_wait(implicit_wait)
    request.cls.driver: WebDriver = driver
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name=request.node.name, attachment_type=AttachmentType.PNG)


def Chrome_Option(request):
    headless_mode = request.config.getoption("--headless")
    option = webdriver.ChromeOptions()
    if headless_mode:
        option.add_argument("headless")

    option.accept_insecure_certs = True
    option.add_argument("–incognito")
    driver = webdriver.Chrome(service=Service(), options=option)
    return driver


def Firefox_Option(request):
    headless_mode = request.config.getoption("--headless")
    option = webdriver.FirefoxOptions()
    if headless_mode:
        option.add_argument("-headless")
    option.accept_insecure_certs = True
    option.add_argument("-private-window")
    driver = webdriver.Firefox(service=Service(), options=option)
    return driver


def Edge_Option(request):
    headless_mode = request.config.getoption("--headless")
    option = webdriver.EdgeOptions()
    if headless_mode:
        option.add_argument("headless")
    option.accept_insecure_certs = True
    option.add_argument("–incognito")
    driver = webdriver.Edge(service=Service(), options=option)
    return driver
