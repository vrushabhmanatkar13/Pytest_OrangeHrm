import allure
import pytest

from tests import testbase
from tests.testbase import TestBase
from uitilites.Logger import get_logger, Step
from uitilites.readProperties import getConfig
from uitilites.read_excle import get_data


#username, password = getConfig().get('Info', 'username'), getConfig().get('Info', 'password')


@allure.feature("Login Page")
class Test_Login(TestBase):
    @allure.title("Verify Title")
    def test_Verify_Title(self, request):
        test_name = get_logger(request.node.name)
        title_name = self.driver.title
        self.assert_equals("OrangeHRM", title_name, test_name)

    @allure.title("Verify Login With Valid Data")
    @pytest.mark.parametrize("username1,password1", get_data("login", "Verify Login with valid data"))
    def test_Verify_Login_ValidData(self, request, username1, password1):
        test_name = get_logger(request.node.name)
        self.loginpage.Login(username1, password1)
        test_name.info(f"Enter username:{username1} and Enter password:{password1}")
        test_name.info("Click login")
        header_text = self.sidebar.get_HeaderText()
        self.assert_equals("Dashboard", header_text, test_name)
        self.assert_not_equals(self.sidebar.get_user_name(), "", test_name)
