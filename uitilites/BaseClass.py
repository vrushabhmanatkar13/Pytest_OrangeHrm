import inspect
import logging

from typing import ClassVar, Union

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from uitilites.Logger import get_logger
from uitilites.readProperties import getConfig

webdriver_wait = float(getConfig().get('static data', 'webdriver_wait'))


# @pytest.mark.usefixtures("Setup_TearDown")
class BaseClass:
    # driver: Union[webdriver.Chrome, webdriver.Firefox, webdriver.Edge, webdriver.Remote]
    # driver: ClassVar[webdriver.Chrome]
    # driver: WebDriver
    def WebdriverWait(self,driver):
        self.wait = WebDriverWait(driver, 20)

    def click(self, driver: WebDriver, webelement):
        log = get_logger("click")
        try:
            element: WebElement = self.wait.until(EC.element_to_be_clickable(
                driver.find_element(webelement[0], webelement[1])))
            element.click()

        except Exception as e:
            log.error("Element Not Found " + str(e).splitlines()[0])

    def click_javsscript(self, driver: WebDriver, webelement):
        log = get_logger("click_javascript")
        try:
            element: WebElement = self.wait.until(EC.element_to_be_clickable(
                driver.find_element(webelement[0], webelement[1])))
            driver.execute_script("arguments[0].click();", element)
        except Exception as e:
            log.error("Element Not Found" + str(e).splitlines()[0])

    def sendkeys(self, driver: WebDriver, webelement, value):
        log = get_logger("sendkeys")
        try:
            element: WebElement = self.wait.until(EC.element_to_be_clickable(
                driver.find_element(webelement[0], webelement[1])))
            element.send_keys(value)
        except Exception as e:
            log.error("Element Not found" + str(e).splitlines()[0])

    def gettext(self, driver: WebDriver, webelement):
        log = get_logger("gettext")
        try:
            element: WebElement = self.wait.until(EC.visibility_of(
                driver.find_element(webelement[0], webelement[1])))
            return element.text
        except Exception as e:
            log.error("Element Not found" + str(e).splitlines()[0])

    def assert_equals(self, Expected, Actual, test_name: logging.Logger):
        assert Expected == Actual, (
            test_name.error(f"Expected: {Expected}, Found: {Actual}")
        )

    def assert_not_equals(self, Expected, Actual, test_name: logging.Logger):
        assert Expected != Actual, (
            test_name.error(f"Expected: {Expected}, Found: {Actual}")
        )

    def assert_True(self, Actual, test_name: logging.Logger):
        assert Actual, (
            test_name.error(f"Expected: True, Found: {Actual} ")
        )

    def assert_False(self, Actual, test_name: logging.Logger):
        assert not Actual, (
            test_name.error(f"Expected: False, Found: {Actual} ")
        )
