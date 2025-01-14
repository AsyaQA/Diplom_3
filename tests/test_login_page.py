from pages.login_page import LoginPage
import allure


class TestLoginPage:

    @allure.title('Проверка перехода на страницу восстановления пароля')
    def test_redirect_to_password_recovery(self, driver):
        login_page = LoginPage(driver)
        login_page.redirect_to_recovery_password_page()
        assert login_page.get_text_recovery_button() == 'Восстановить'

    @allure.title('Проверка ввода почты и клика на кнопку "Восстановить"')
    def test_input_email(self, driver):
        login_page = LoginPage(driver)
        login_page.redirect_to_recovery_password_page()
        login_page.change_password()
        assert login_page.get_text_from_save_button() == 'Сохранить'

    @allure.title('Проверка подсветки поля показа\скрытия пароля')
    def test_highlighted_password_field(self, driver):
        login_page = LoginPage(driver)
        login_page.redirect_to_recovery_password_page()
        login_page.change_password()
        login_page.click_to_show_hide_button()
        assert 'placeholder-focused' in login_page.get_class_from_password_field()




