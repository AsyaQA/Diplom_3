import allure

from locators.order_list_page_locators import OrderListPageLocators
from pages.base_page import BasePage


class OrderListPage(BasePage):

    @allure.step('Получаем текст для аасерта теста: переход на страницу лента заказов')
    def control_text_on_order_page(self):
        return self.get_text_from_element(OrderListPageLocators.TEXT_ON_ORDER_LIST_PAGE)

    @allure.step('Открываем модальное окно с информацией о заказе')
    def open_order_info(self):
        self.click_to_the_element(OrderListPageLocators.ORDER_INFO_MODAL)

    @allure.step('Получаем текст для ассерта теста: открытие модального окна с информацией о заказе')
    def control_element_in_modal(self):
        return self.get_text_from_element(OrderListPageLocators.TEXT_ON_MODAL_WINDOW)

    @allure.step('Получаем номер заказа пользователя в ленте заказов')
    def find_user_order(self, text):
        formated_locator = self.format_locator(OrderListPageLocators.ORDER_USER, text)
        return self.get_text_from_element(formated_locator)

    @allure.step('Получаем текст с счетчика "Выполнено за все время"')
    def counter_for_all_time_orders(self):
        return self.get_text_from_element(OrderListPageLocators.COMPLETED_FOR_ALL_TIME)

    @allure.step('Получаем текст с счетчика "Выполнено за сегодня"')
    def counter_for_today_orders(self):
        return self.get_text_from_element(OrderListPageLocators.COMPLETED_FOR_TODAY)

    @allure.step('Проверяем, что созданный заказ с определенным номером отображается в статусе "В работе"')
    def get_list_status_at_work(self):
        self.control_text_on_order_page()
        self.find_element_change_text(OrderListPageLocators.AT_WORK_STATUS, 'Все текущие заказы готовы!')
        return self.get_text_from_element(OrderListPageLocators.AT_WORK_STATUS)
