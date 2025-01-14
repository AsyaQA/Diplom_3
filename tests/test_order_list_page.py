from pages.account_page import AccountPage
from pages.kit_page import KitPage
from pages.login_page import LoginPage
from pages.order_list_page import OrderListPage
import allure


class TestOrderListPage:

    @allure.title('Проверка перехода на страницу лента заказов')
    def test_redirect_to_order_list(self, driver):
        order_list = OrderListPage(driver)
        kit_page = KitPage(driver)
        kit_page.click_to_the_order_list_button()
        assert order_list.control_text_on_order_page() == 'Лента заказов'

    @allure.title('Проверка открытия окна с деталями заказа')
    def test_open_modal_with_order_info(self, driver):
        order_list = OrderListPage(driver)
        kit_page = KitPage(driver)
        kit_page.click_to_the_order_list_button()
        order_list.open_order_info()
        assert order_list.control_element_in_modal() == 'Cостав'

    @allure.title('Проверка, что заказ из истории заказов пользователя отображается в Ленте заказов')
    def test_order_from_user_history_displayed_in_order_list(self, driver):
        order_list = OrderListPage(driver)
        account_page = AccountPage(driver)
        login_page = LoginPage(driver)
        kit_page = KitPage(driver)
        login_page.login_to_account()
        kit_page.create_order()
        kit_page.click_to_personal_account()
        account_page.redirect_to_order_history()
        number_order = account_page.get_last_order_number()
        kit_page.click_to_the_order_list_button()
        assert order_list.find_user_order(number_order) == number_order


    @allure.title('Проверка, что счетчик "выполнено за всё время" увеличивается с каждым заказом')
    def test_counter_for_all_time_orders_has_increased(self, driver):
        order_list = OrderListPage(driver)
        account_page = AccountPage(driver)
        login_page = LoginPage(driver)
        kit_page = KitPage(driver)
        login_page.login_to_account()
        kit_page.click_to_the_order_list_button()
        all_time_orders_old = order_list.counter_for_all_time_orders()
        account_page.redirect_to_kit_page()
        kit_page.create_order()
        kit_page.click_to_the_order_list_button()
        all_time_orders_new = order_list.counter_for_all_time_orders()
        assert all_time_orders_new > all_time_orders_old

    @allure.title('Проверка, что счетчик "выполнено за сегодня" увеличивается с каждым заказом')
    def test_counter_for_today_orders_has_increased(self, driver):
        order_list = OrderListPage(driver)
        account_page = AccountPage(driver)
        login_page = LoginPage(driver)
        kit_page = KitPage(driver)
        login_page.login_to_account()
        kit_page.click_to_the_order_list_button()
        today_orders_old = order_list.counter_for_today_orders()
        account_page.redirect_to_kit_page()
        kit_page.create_order()
        kit_page.click_to_the_order_list_button()
        today_orders_new = order_list.counter_for_today_orders()
        assert today_orders_new > today_orders_old

    @allure.title('Проверка, что созданный заказ находится в статусе "В работе"')
    def test_new_order_in_at_work_status(self, driver):
        order_list = OrderListPage(driver)
        login_page = LoginPage(driver)
        kit_page = KitPage(driver)
        login_page.login_to_account()
        order_number = kit_page.create_order()
        kit_page.click_to_the_order_list_button()
        assert order_number in order_list.get_list_status_at_work()


