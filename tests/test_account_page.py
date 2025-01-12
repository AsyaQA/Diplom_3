from pages.account_page import AccountPage
from pages.kit_page import KitPage
from pages.login_page import LoginPage
import allure


class TestAccountPage:

    @allure.title('Проверка перехода в личный кабинет')
    def test_redirect_to_personal_account(self, driver):
        account_page = AccountPage(driver)
        login_page = LoginPage(driver)
        kit_page = KitPage(driver)
        login_page.login_to_account()
        kit_page.click_to_personal_account()
        assert account_page.get_exit_text() == 'Выход'

    @allure.title('Проверка перехода историю заказов личного кабинета')
    def test_redirect_to_order_history(self, driver):
        account_page = AccountPage(driver)
        login_page = LoginPage(driver)
        kit_page = KitPage(driver)
        login_page.login_to_account()
        kit_page.click_to_personal_account()
        account_page.redirect_to_order_history()
        assert 'Account_link_active' in account_page.get_class_from_order_history()

    @allure.title('Проверка выхода из аккаунта')
    def test_logout_from_account(self, driver):
        account_page = AccountPage(driver)
        login_page = LoginPage(driver)
        kit_page = KitPage(driver)
        login_page.login_to_account()
        kit_page.click_to_personal_account()
        account_page.logout_from_account()
        assert login_page.control_text_on_the_page() == 'Вход'


