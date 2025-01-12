import data
from locators.kit_page_locators import KitPageLocators
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage



class KitPage(BasePage):

    # method for open and close ingredient modal windows
    def open_ingredient_info(self, locator):
        if data.DRIVER_NAME == 'firefox':
            self.wait_for_disappears_element_for_firefox(
                LoginPageLocators.CLICK_INTERCEPTING_WINDOW
            )
        self.click_to_the_element(locator)

    def close_ingredient_info(self):
        if data.DRIVER_NAME == 'firefox':
            self.wait_for_disappears_element_for_firefox(
                LoginPageLocators.CLICK_INTERCEPTING_WINDOW
            )
        self.click_to_the_element(KitPageLocators.MODAL_CLOSE_BUTTON)

    def get_attribute_from_modal_info_window(self):
        return self.find_element_without_wait(KitPageLocators.CLOSE_MODAL_INFO_WINDOW).get_attribute('class')

    # method to redirect to personal account
    def click_to_personal_account(self):
        if data.DRIVER_NAME == 'firefox':
            self.wait_for_disappears_element_for_firefox(
                LoginPageLocators.CLICK_INTERCEPTING_WINDOW
            )
        self.click_to_the_element(KitPageLocators.PERSONAL_ACCOUNT_BUTTON)

    # method to redirect to order list
    def click_to_the_order_list_button(self):
        if data.DRIVER_NAME == 'firefox':
            self.wait_for_disappears_element_for_firefox(
                LoginPageLocators.CLICK_INTERCEPTING_WINDOW
            )
        self.click_to_the_element(KitPageLocators.LIST_OF_ORDERS_BUTTON)

    # method to control redirect to kit page
    def control_redirect_to_kit_page(self):
        return self.get_text_from_element(KitPageLocators.KRATORNAYA_BUN_N_200I)

    # methods for drag and drop
    def drag_and_drop_ingredients(self, locator):
        if data.DRIVER_NAME == 'firefox':
            self.move_the_element_for_firefox(
                self.find_element_with_wait(locator),
                self.find_element_with_wait(KitPageLocators.BASKET)
            )
        else:
            self.move_the_element(locator, KitPageLocators.BASKET)

    # method to click set order button and create order
    def set_order(self):
        self.drag_and_drop_ingredients(KitPageLocators.FLUORESCENT_BUN_R2_D3)
        if data.DRIVER_NAME == 'firefox':
            self.wait_for_disappears_element_for_firefox(
                LoginPageLocators.CLICK_INTERCEPTING_WINDOW
            )
        self.click_to_the_element(KitPageLocators.SET_ORDER)

    # method to control id order
    def control_id_order(self):
        self.find_element_change_text(KitPageLocators.ID_ORDER, '9999')
        return self.get_text_from_element(KitPageLocators.ID_ORDER)

    # method with all steps to set order
    def create_order(self):
        self.set_order()
        order_number = self.control_id_order()
        self.close_ingredient_info()
        return order_number
