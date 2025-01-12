from selenium.webdriver.common.by import By


class AccountPageLocators:

    ORDER_HISTORY_BUTTON = By.XPATH, '//*[text()="История заказов"]'
    EXIT_BUTTON = By.XPATH, '//*[text()="Выход"]'
    ACTIVE_ORDER_HISTORY = By.XPATH, '//*[@href="/account/order-history"]'
    CANCEL_BUTTON = By.XPATH, '//*[text()="Отмена"]'
    LAST_ORDER_NUMBER = By.XPATH , '//ul/li[last()]/a/div/p[@class="text text_type_digits-default"]'



