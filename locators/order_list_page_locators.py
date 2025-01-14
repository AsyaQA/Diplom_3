from selenium.webdriver.common.by import By


class OrderListPageLocators:

    TEXT_ON_ORDER_LIST_PAGE = By.XPATH, '//*[text()="Лента заказов"]'
    TEXT_ON_MODAL_WINDOW = By.XPATH, '//*[text()="Cостав"]'

    # modal window with order info
    ORDER_INFO_MODAL = By.XPATH, '//*[contains(@class, "OrderHistory_link")]'
    CLOSE_INFO_MODAL = By.XPATH, '//section[contains(@class, "Modal_modal_opened")]/div/button'

    # locator for order number
    ORDER_USER = By.XPATH, '//p[text()="{}"]'

    # locators for completed order
    COMPLETED_FOR_ALL_TIME = By.XPATH, '//div[@class="undefined mb-15"]/p[contains(@class, "OrderFeed_number")]'
    COMPLETED_FOR_TODAY = By.XPATH, '//div[last()]/p[contains(@class, "OrderFeed_number")]'

    # locators for order in at work status
    AT_WORK_STATUS = By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]/li'
