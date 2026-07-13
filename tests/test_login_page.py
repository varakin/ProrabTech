import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Login page functional")
class TestLoginPage(BaseTest):
    
    @allure.title("Login + Exit")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_exit(self):
        self.login_page.open()
        self.login_page.loader_invisible_login_page()
        self.login_page.is_opened()
        self.login_page.enter_email(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_enter_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_profile_button()
        self.profile_page.is_opened()
        self.profile_page.click_exit_button()
        self.login_page.is_opened()
        self.login_page.make_screenshot("Positive Autorization and Exit success")

        
