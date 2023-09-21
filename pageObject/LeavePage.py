import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class LeavePageObject:
    def __init__(self, driver, baseclass):
        self.driver: WebDriver = driver
        self.baseclass = baseclass

    buttons_tabs= (By.XPATH,"//li[contains(@class,'oxd-topbar-body-nav-tab')]")
    @allure.step('Click "{text}"')
    def click_tabs(self, text):
        tabs = self.driver.find_elements(*LeavePageObject.buttons_tabs)
        for tab in tabs:
            if tab.text == text:
                tab.click()
                break

    def Apply_Leave(self):
        self.click_tabs("Appy")

