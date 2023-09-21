import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class SideBarPage:
    def __init__(self, driver, baseclass):
        self.driver: WebDriver = driver
        self.baseclass = baseclass

    label_header_text = (By.XPATH, "//div[@class='oxd-topbar-header-title']")
    label_user_name = (By.XPATH, "//p[@class='oxd-userdropdown-name']")
    sidebar_button = (By.XPATH, "//li[@class='oxd-main-menu-item-wrapper']//span")

    @allure.step("Get Header Text")
    def get_HeaderText(self):
        return self.baseclass.gettext(self.driver, self.label_header_text)

    @allure.step("Get UserName")
    def get_user_name(self):
        return self.baseclass.gettext(self.driver, self.label_user_name)

    @allure.step('Click "{text}"')
    def click_sidebar_option(self, text):
        option_list = self.driver.find_elements(*SideBarPage.sidebar_button)
        for a in option_list:
            if a.text == text:
                a.click()
                break
