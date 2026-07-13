import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):

    PAGE_URL = Links.LOGIN_PAGE

    USERNAME_FIELD = (By.XPATH, "//input[@name='email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    REGISTRATION_BUTTON = (By.XPATH, "//a[@class='outlined medium button sign-up-button']")
    SPINNER = (By.XPATH, "//dialog[@class='loading-dialog']")

    @allure.step("Enter login")
    def enter_email(self, login):
        self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD)).send_keys(login)

    @allure.step("Enter password")
    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)

    @allure.step("Click Enter button")
    def click_enter_button(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()

    @allure.step("Wait until loader visible")
    def loader_invisible_login_page(self):
        self.wait.until(EC.presence_of_element_located(self.USERNAME_FIELD))
        self.wait.until(EC.invisibility_of_element_located(self.SPINNER))

