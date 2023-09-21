import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class MyInfoPageObject:
    def __init__(self, driver, baseclass):
        self.driver: WebDriver = driver
        self.baseclass = baseclass

    label_name = (By.XPATH, "//h6[@class='oxd-text oxd-text--h6 --strong']")
    textbox_firstname = (By.XPATH, "//input[@placeholder='First Name']")
    textbox_lastname = (By.XPATH, "//input[@placeholder='Last Name']")

    @allure.step("Get User Name")
    def Verify_My_info(self):
        name_text = self.baseclass.gettext(self.driver, self.label_name)
        return name_text
