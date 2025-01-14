import allure

import data
from locators.kit_page_locators import KitPageLocators
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage



class KitPage(BasePage):

    @allure.step('Открываем модальное окно с информацией об ингредиенте')
    def open_ingredient_info(self, locator):
        if data.DRIVER_NAME == 'firefox':
            self.wait_for_disappears_element_for_firefox(
                LoginPageLocators.CLICK_INTERCEPTING_WINDOW
            )
        self.click_to_the_element(locator)

    @allure.step('Закрываем модальное окно с информацией об ингредиенте')
    def close_ingredient_info(self):
        if data.DRIVER_NAME == 'firefox':
            self.wait_for_disappears_element_for_firefox(
                LoginPageLocators.CLICK_INTERCEPTING_WINDOW
            )
        self.click_to_the_element(KitPageLocators.MODAL_CLOSE_BUTTON)

    @allure.step('Получаем атрибут класса для ассерта теста с закрытием модального окна')
    def get_attribute_from_modal_info_window(self):
        return self.find_element_without_wait(KitPageLocators.CLOSE_MODAL_INFO_WINDOW).get_attribute('class')

    @allure.step('Переходим в личный кабинет')
    def click_to_personal_account(self):
        if data.DRIVER_NAME == 'firefox':
            self.wait_for_disappears_element_for_firefox(
                LoginPageLocators.CLICK_INTERCEPTING_WINDOW
            )
        self.click_to_the_element(KitPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Переходим на ленту заказов')
    def click_to_the_order_list_button(self):
        if data.DRIVER_NAME == 'firefox':
            self.wait_for_disappears_element_for_firefox(
                LoginPageLocators.CLICK_INTERCEPTING_WINDOW
            )
        self.click_to_the_element(KitPageLocators.LIST_OF_ORDERS_BUTTON)

    @allure.step('Проверяем, что находимся на странице конструктора')
    def control_redirect_to_kit_page(self):
        return self.get_text_from_element(KitPageLocators.KRATORNAYA_BUN_N_200I)

    @allure.step('Перетягиваем ингридиенты в корзину')
    def drag_and_drop_ingredients(self, locator):
        if data.DRIVER_NAME == 'firefox':
            self.move_the_element_for_firefox(
                self.find_element_with_wait(locator),
                self.find_element_with_wait(KitPageLocators.BASKET)
            )
        else:
            self.move_the_element(locator, KitPageLocators.BASKET)

    @allure.step('Перетягиваем ингредиенты и нажимаем на кнопку создания заказа')
    def set_order(self):
        self.drag_and_drop_ingredients(KitPageLocators.FLUORESCENT_BUN_R2_D3)
        if data.DRIVER_NAME == 'firefox':
            self.wait_for_disappears_element_for_firefox(
                LoginPageLocators.CLICK_INTERCEPTING_WINDOW
            )
        self.click_to_the_element(KitPageLocators.SET_ORDER)

    @allure.step('Проверяем, что номер заказа отличен от 9999')
    def control_id_order(self):
        self.find_element_change_text(KitPageLocators.ID_ORDER, '9999')
        return self.get_text_from_element(KitPageLocators.ID_ORDER)

    @allure.step('Создаем заказ')
    def create_order(self):
        self.set_order()
        order_number = self.control_id_order()
        self.close_ingredient_info()
        return order_number
