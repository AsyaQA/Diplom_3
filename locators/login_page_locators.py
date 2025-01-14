from selenium.webdriver.common.by import By


class LoginPageLocators:

    # locators for recovery password
    LINK_TO_RESET_PASSWORD = By.XPATH, '//*[text()="Восстановить пароль"]'
    ENTERING_EMAIL = By.XPATH, '//*[@type="text"]'
    RECOVER_BUTTON = By.XPATH, '//*[text()="Восстановить"]'
    SAVE_BUTTON = By.XPATH, '//*[text()="Сохранить"]'
    ICON_TO_VISIBLE_PASSWORD = By.XPATH, '//fieldset[contains(@class, "Auth_fieldset")]/div/div/div'
    PASSWORD_FIELD_LABLE = By.XPATH,'//fieldset[contains(@class, "Auth_fieldset")]/div/div/label[text()="Пароль"]'

    # locator who intercepting click in firefox on recovery password page
    CLICK_INTERCEPTING_WINDOW = By.XPATH, '//div[contains(@class, "Modal_modal")]/div[contains(@class, "Modal_modal_overlay")]'

    # locators for login in account
    EMAIL = By.XPATH, '//*[@type="text"]'
    PASSWORD = By.XPATH, '//*[@type="password"]'
    LOGIN_BUTTON = By.XPATH, '//*[text()="Войти"]'
    TEXT_ENTRANCE = By.XPATH, '//*[text()="Вход"]'


