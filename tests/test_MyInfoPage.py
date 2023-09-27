import time

import allure
import pytest
from allure_commons.types import AttachmentType


from tests.testbase import TestBase
from uitilites.Logger import get_logger
from uitilites.read_excle import get_data_by_index


@allure.feature("My Info Page")
class TestMyInfoPage(TestBase):
    @allure.title("Verify Name")
    def test_Verify_MyInfo(self, request):
        test_name = get_logger(request.node.name)
        data = get_data_by_index("login", 3)
        self.loginpage.Login(data[0], data[1])
        text_username = self.sidebar.get_user_name()
        test_name.info(f"UserName: {text_username} (Header)")
        self.sidebar.click_sidebar_option("My Info")
        test_name.info("Click My Info")
        header_text = self.sidebar.get_HeaderText()
        time.sleep(1)
        label_username = self.myinfo.Verify_My_info()
        test_name.info(f"Username:{label_username} (My Info)")
        self.assert_equals("PIM", header_text, test_name)
        self.assert_equals(text_username, label_username, test_name)
