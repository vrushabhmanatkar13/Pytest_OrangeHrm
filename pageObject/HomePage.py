import time

import allure

import tests.testbase as test_base
# Avoid Circular import Error use import package/module as variable
# using this variable we can access methods
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pageObject.SideBar_Header import SideBarPage


class HomePageObject:
    def __init__(self, driver, baseclass):
        self.driver: WebDriver = driver
        self.baseclass = baseclass

    label_puch_text = (By.XPATH, "//p[@class='oxd-text oxd-text--p orangehrm-attendance-card-state']")
    button_watch = (By.CSS_SELECTOR, "i[class='oxd-icon bi-stopwatch']")
    textbox_time = (By.XPATH, "//input[@placeholder='hh:mm']")
    button_out = (By.XPATH, "//button[normalize-space()='Out']")
    button_in = (By.XPATH, "//button[normalize-space()='In']")
    label_success = (By.XPATH, "//p[text()='Success']")

    @allure.step("Get Punched Text")
    def get_puch_text(self):
        self.driver.refresh()
        return self.baseclass.gettext(self.driver, self.label_puch_text)

    @allure.step("Click watch")
    @allure.step("Click Out")
    def puch_out_user(self, sidebar: SideBarPage):
        self.baseclass.click(self.driver, self.button_watch)
        header_text = sidebar.get_HeaderText()
        time.sleep(1)
        self.baseclass.click_javsscript(self.driver, self.button_out)

        success_text = self.baseclass.gettext(self.driver, self.label_success)
        sidebar.click_sidebar_option("Dashboard")
        return header_text, success_text

    @allure.step("Click watch")
    @allure.step("Click In")
    def puch_in_user(self, sidebar: SideBarPage):
        self.baseclass.click(self.driver, self.button_watch)
        time.sleep(1)
        self.baseclass.click_javsscript(self.driver, self.button_in)
        success_text = self.baseclass.gettext(self.driver, self.label_success)
        sidebar.click_sidebar_option("Dashboard")
        return success_text
