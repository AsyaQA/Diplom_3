import allure

import data
from locators.account_page_locators import AccountPageLocators
from locators.kit_page_locators import KitPageLocators
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class AccountPage(BasePage):

    @allure.step('Переходим на страницу "История заказов" в личном кабинете')
    def redirect_to_order_history(self):
        if data.DRIVER_NAME == 'firefox':
            self.wait_for_disappears_element_for_firefox(
                LoginPageLocators.CLICK_INTERCEPTING_WINDOW
            )
        self.click_to_the_element(AccountPageLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Получаем атрибут класса для истории заказов для ассерта')
    def get_class_from_order_history(self):
        return self.find_element_with_wait(AccountPageLocators.ACTIVE_ORDER_HISTORY).get_attribute('class')

    @allure.step('Получаем текст с кнопки "Выход" для ассерта')
    def get_exit_text(self):
        return self.get_text_from_element(AccountPageLocators.EXIT_BUTTON)

    @allure.step('Нажимаем на кнопку "Выход"')
    def logout_from_account(self):
        if data.DRIVER_NAME == 'firefox':
            self.wait_for_disappears_element_for_firefox(
                LoginPageLocators.CLICK_INTERCEPTING_WINDOW
            )
        self.click_to_the_element(AccountPageLocators.EXIT_BUTTON)

    @allure.step('Переходим на страницу "Конструктор"')
    def redirect_to_kit_page(self):
        self.click_to_the_element(KitPageLocators.KIT_BUTTON)

    @allure.step('Получаем номер последнего заказа пользователя')
    def get_last_order_number(self):
        return self.get_text_from_element(AccountPageLocators.LAST_ORDER_NUMBER)
