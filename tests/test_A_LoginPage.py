from tests import testbase
from tests.testbase import TestBase
from uitilites.Logger import get_logger
from uitilites.readProperties import getConfig

username, password = getConfig().get('Info', 'username'), getConfig().get('Info', 'password')





class Test_Login(TestBase):

    def test_Verify_Title(self, request):
        test_name = get_logger(request.node.name)
        title_name = self.driver.title
        self.assert_equals("OrangeHRM", title_name, test_name)

    def test_Verify_Login_ValidData(self, request):
        test_name = get_logger(request.node.name)
        self.loginpage.Login(username, password)
        test_name.info(f"Enter username:{username} and Enter password:{password}")
        test_name.info("Click login")
        header_text = self.sidebar.get_HeaderText()
        self.assert_equals("Dashboard", header_text, test_name)
        self.assert_not_equals(self.sidebar.get_user_name(), "", test_name)
