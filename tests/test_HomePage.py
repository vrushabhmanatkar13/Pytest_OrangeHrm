import allure
import pytest


from tests.testbase import TestBase
from uitilites.Logger import get_logger
from uitilites.read_excle import get_data_by_index


@allure.feature("HomePage")
class TestHomePage(TestBase):
    @allure.title("Verify Puch out user")
    def test_Verify_puch_out_user(self, request):
        test_name = get_logger(request.node.name)
        data = get_data_by_index("login", 3)
        self.loginpage.Login(data[0], data[1])
        text_in = self.homepage.get_puch_text()
        header_text, success_text = self.homepage.puch_out_user(self.sidebar)
        test_name.info("Click watch icon")
        test_name.info("Click Punch out Button")
        test_name.info("Click Dashboard")
        text_out = self.homepage.get_puch_text()

        self.assert_equals("Attendance", header_text, test_name)
        self.assert_equals("Success", success_text, test_name)
        self.assert_not_equals(text_out, text_in, test_name)

    @allure.title("Verify Puch In user")
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
