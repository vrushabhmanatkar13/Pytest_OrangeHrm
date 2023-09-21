import allure
import pytest

from tests import testbase
from tests.testbase import TestBase
from uitilites.Logger import get_logger, Step
from uitilites.readProperties import getConfig

username, password = getConfig().get('Info', 'username'), getConfig().get('Info', 'password')


@allure.description("Login Page Test Cases")
@allure.feature("Login")
@pytest.mark.usefixtures("log_on_failure")
class Test_Login(TestBase):
    @allure.title("Verify Title")
    def test_Verify_Title(self, request):
        test_name = get_logger(request.node.name)
        title_name = self.driver.title
        self.assert_equals("OrangeHRM", title_name, test_name)

    @allure.title("Verify Login With Valid Data")
    def test_Verify_Login_ValidData(self, request):
        test_name = get_logger(request.node.name)
        self.loginpage.Login(username, password)
        test_name.info(f"Enter username:{username} and Enter password:{password}")
        # Step(f"Enter username:{username} and Enter password:{password}")
        test_name.info("Click login")
        # Step("Click login")
        header_text = self.sidebar.get_HeaderText()
        self.assert_equals("Dashboard", header_text, test_name)
        self.assert_not_equals(self.sidebar.get_user_name(), "", test_name)
