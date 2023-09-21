import allure
import pytest

from tests.test_A_LoginPage import username, password
from tests.testbase import TestBase
from uitilites.Logger import get_logger

@pytest.mark.usefixtures("log_on_failure")
class TestHomePage(TestBase):

    def test_Verify_puch_out_user(self, request):
        test_name = get_logger(request.node.name)
        self.loginpage.Login(username, password)
        text_in = self.homepage.get_puch_text()
        header_text, success_text = self.homepage.puch_out_user(self.sidebar)
        test_name.info("Click watch icon")
        test_name.info("Click Punch out Button")
        test_name.info("Click Dashboard")
        text_out = self.homepage.get_puch_text()

        self.assert_equals("Attendance", header_text, test_name)
        self.assert_equals("Success", success_text, test_name)
        self.assert_not_equals(text_out, text_in, test_name)


    def test_Verify_punch_In_user(self, request):
        test_name = get_logger(request.node.name)
        text_out = self.homepage.get_puch_text()
        success_text = self.homepage.puch_in_user(self.sidebar)
        test_name.info("Click watch icon")
        test_name.info("Click Punch in Button")
        test_name.info("Click Dashboard")
        text_in = self.homepage.get_puch_text()

        self.assert_equals("Success", success_text, test_name)
        self.assert_not_equals(text_out, text_in, test_name)
