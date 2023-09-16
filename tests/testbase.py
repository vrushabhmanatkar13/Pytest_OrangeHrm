import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from pageObject.HomePage import HomePageObject
from pageObject.LoginPage import LoginPageObject
from pageObject.MyInfoPage import MyInfoPageObject
from pageObject.SideBar_Header import SideBarPage
from tests.conftest import Setup_TearDown

from uitilites.BaseClass import BaseClass


@pytest.mark.usefixtures("Setup_TearDown")
class TestBase(BaseClass):
    driver: WebDriver

    @pytest.fixture(autouse=True)
    def class_objects(self):
        self.baseclass = BaseClass()
        self.baseclass.WebdriverWait(Setup_TearDown)
        self.sidebar = SideBarPage(self.driver, self.baseclass)
        self.loginpage = LoginPageObject(self.driver, self.baseclass)
        self.homepage = HomePageObject(self.driver, self.baseclass)
        self.myinfo = MyInfoPageObject(self.driver, self.baseclass)
