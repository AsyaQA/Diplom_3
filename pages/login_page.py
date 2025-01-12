import data
import helpers
from locators.login_page_locators import LoginPageLocators
from locators.kit_page_locators import KitPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    # all methods only for login page tests
    def redirect_to_recovery_password_page(self):
        self.click_to_the_element(KitPageLocators.PERSONAL_ACCOUNT_BUTTON)
        self.click_to_the_element(LoginPageLocators.LINK_TO_RESET_PASSWORD)

    def get_text_recovery_button(self):
        return self.get_text_from_element(LoginPageLocators.RECOVER_BUTTON)

    def change_password(self):
        self.add_text_in_element(LoginPageLocators.ENTERING_EMAIL, helpers.get_random_email())
        self.click_to_the_element(LoginPageLocators.RECOVER_BUTTON)

    def get_text_from_save_button(self):
        return self.get_text_from_element(LoginPageLocators.SAVE_BUTTON)

    def click_to_show_hide_button(self):
        if data.DRIVER_NAME == 'firefox':
            self.wait_for_disappears_element_for_firefox(
                LoginPageLocators.CLICK_INTERCEPTING_WINDOW
            )
        self.click_to_the_element(LoginPageLocators.ICON_TO_VISIBLE_PASSWORD)

    def get_class_from_password_field(self):
        return self.find_element_with_wait(LoginPageLocators.PASSWORD_FIELD_LABLE).get_attribute('class')

    def login_to_account(self):
        if data.DRIVER_NAME == 'firefox':
            self.wait_for_disappears_element_for_firefox(
                LoginPageLocators.CLICK_INTERCEPTING_WINDOW
            )
        self.click_to_the_element(KitPageLocators.PERSONAL_ACCOUNT_BUTTON)
        self.add_text_in_element(LoginPageLocators.EMAIL, data.email)
        self.add_text_in_element(LoginPageLocators.PASSWORD, data.password)
        self.click_to_the_element(LoginPageLocators.LOGIN_BUTTON)

    def control_text_on_the_page(self):
        return self.get_text_from_element(LoginPageLocators.TEXT_ENTRANCE)
