import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class ProfilePage(BasePage):

    PAGE_URL = Links.PROFILE_PAGE

    EXIT_BUTTON = (By.XPATH, "//button[@class='subtle medium button']")

    @allure.step("Click exit button")
    def click_exit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.EXIT_BUTTON)).click()