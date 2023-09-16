import os.path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from uitilites.Logger import setup_logging
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
    browser_name: [str] = request.config.getoption("--browsername")
    if browser_name.lower() == "chrome":
        driver = Chrome_Option(request)
    elif browser_name.lower() == "firefox":
        driver = Firefox_Option(request)
    elif browser_name.lower() == "edge":
        driver = Edge_Option(request)
    else:
        raise Exception("Browser not Present")

    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(implicit_wait)
    request.cls.driver: WebDriver = driver
    yield driver
    driver.quit()


@pytest.fixture(autouse=True)
def wait(Setup_TearDown):
    return WebDriverWait(Setup_TearDown, 10)


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


