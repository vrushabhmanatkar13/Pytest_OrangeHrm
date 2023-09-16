import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from uitilites.BaseClass import BaseClass


class LoginPageObject:

    def __init__(self, driver, baseclass):
        self.driver: WebDriver = driver
        self.baseclass = baseclass

    textbox_username = (By.XPATH, "//input[@name='username']")
    textbox_password = (By.XPATH, "//input[@name='password']")
    button_login = (By.XPATH, "//button[@type='submit']")

    def Login(self, username, password):
        self.baseclass.sendkeys(self.driver,self.textbox_username, username)
        self.baseclass.sendkeys(self.driver,self.textbox_password, password)
        self.baseclass.click(self.driver, self.button_login)
