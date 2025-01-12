import data
from locators.account_page_locators import AccountPageLocators
from locators.kit_page_locators import KitPageLocators
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class AccountPage(BasePage):

    # methods for test in account page (redirect, logout)
    def redirect_to_order_history(self):
        if data.DRIVER_NAME == 'firefox':
            self.wait_for_disappears_element_for_firefox(
                LoginPageLocators.CLICK_INTERCEPTING_WINDOW
            )
        self.click_to_the_element(AccountPageLocators.ORDER_HISTORY_BUTTON)

    def get_class_from_order_history(self):
        return self.find_element_with_wait(AccountPageLocators.ACTIVE_ORDER_HISTORY).get_attribute('class')

    def get_exit_text(self):
        return self.get_text_from_element(AccountPageLocators.EXIT_BUTTON)

    def logout_from_account(self):
        if data.DRIVER_NAME == 'firefox':
            self.wait_for_disappears_element_for_firefox(
                LoginPageLocators.CLICK_INTERCEPTING_WINDOW
            )
        self.click_to_the_element(AccountPageLocators.EXIT_BUTTON)

    # method to redirect to kit page
    def redirect_to_kit_page(self):
        self.click_to_the_element(KitPageLocators.KIT_BUTTON)

    # method to get last order number
    def get_last_order_number(self):
        return self.get_text_from_element(AccountPageLocators.LAST_ORDER_NUMBER)
