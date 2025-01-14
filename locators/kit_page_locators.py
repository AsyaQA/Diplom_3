from selenium.webdriver.common.by import By


class KitPageLocators:

    # buns
    FLUORESCENT_BUN_R2_D3 = By.XPATH, '//*[text()="Флюоресцентная булка R2-D3"]'
    KRATORNAYA_BUN_N_200I = By.XPATH, '//*[text()="Краторная булка N-200i"]'

    # sauces
    SPICY_X_SAUCE = By.XPATH, '//*[text()="Соус Spicy-X"]'
    SPACE_SAUCE = By.XPATH, '//*[text()="Соус фирменный Space Sauce"]'
    TRADITIONAL_GALACTIC_SAUCE = By.XPATH, '//*[text()="Соус традиционный галактический"]'
    ANTARIAN_FLATWALKER_SAUCE = By.XPATH, '//*[text()="Соус с шипами Антарианского плоскоходца"]'

    # fillings
    PROTOSTOMIA_MEAT = By.XPATH, '//*[text()="Мясо бессмертных моллюсков Protostomia"]'
    BEEF_CHOP = By.XPATH, '//*[text()="Говяжий метеорит (отбивная)"]'
    BIO_CUTLET_MAGNOLIA = By.XPATH, '//*[text()="Биокотлета из марсианской Магнолии"]'
    FILLET_OF_LUMINESCENT = By.XPATH, '//*[text()="Филе Люминесцентного тетраодонтимформа"]'
    CRISPY_RINGS = By.XPATH, '//*[text()="Хрустящие минеральные кольца"]'
    FRUITS_OF_FALLENIAN_TREE = By.XPATH, '//*[text()="Плоды Фалленианского дерева"]'
    MARTIAN_CRYSTALS = By.XPATH, '//*[text()="Кристаллы марсианских альфа-сахаридов"]'
    MINI_SALAD = By.XPATH, '//*[text()="Мини-салат Экзо-Плантаго"]'
    BLUE_CHEESE = By.XPATH, '//*[text()="Сыр с астероидной плесенью"]'

    # counters locators
    FLUORESCENT_COUNTER = By.XPATH, f'{FLUORESCENT_BUN_R2_D3[1]}/parent::a/div/p'
    KRATORNAYA_COUNTER = By.XPATH, f'{KRATORNAYA_BUN_N_200I[1]}/parent::a/div/p'
    SPICY_X_SAUCE_COUNTER = By.XPATH, f'{SPICY_X_SAUCE[1]}/parent::a/div/p'
    SPACE_SAUCE_COUNTER = By.XPATH, f'{SPACE_SAUCE[1]}/parent::a/div/p'
    TRADITIONAL_GALACTIC_SAUCE_COUNTER = By.XPATH, f'{TRADITIONAL_GALACTIC_SAUCE[1]}/parent::a/div/p'
    ANTARIAN_FLATWALKER_SAUCE_COUNTER = By.XPATH, f'{ANTARIAN_FLATWALKER_SAUCE[1]}/parent::a/div/p'
    PROTOSTOMIA_MEAT_COUNTER = By.XPATH, f'{PROTOSTOMIA_MEAT[1]}/parent::a/div/p'
    BEEF_CHOP_COUNTER = By.XPATH, f'{BEEF_CHOP[1]}/parent::a/div/p'
    BIO_CUTLET_MAGNOLIA_COUNTER = By.XPATH, f'{BIO_CUTLET_MAGNOLIA[1]}/parent::a/div/p'
    FILLET_OF_LUMINESCENT_COUNTER = By.XPATH, f'{FILLET_OF_LUMINESCENT[1]}/parent::a/div/p'
    CRISPY_RINGS_COUNTER = By.XPATH, f'{CRISPY_RINGS[1]}/parent::a/div/p'
    FRUITS_OF_FALLENIAN_TREE_COUNTER = By.XPATH, f'{FRUITS_OF_FALLENIAN_TREE[1]}/parent::a/div/p'
    MARTIAN_CRYSTALS_COUNTER = By.XPATH, f'{MARTIAN_CRYSTALS[1]}/parent::a/div/p'
    MINI_SALAD_COUNTER = By.XPATH, f'{MINI_SALAD[1]}/parent::a/div/p'
    BLUE_CHEESE_COUNTER = By.XPATH, f'{BLUE_CHEESE[1]}/parent::a/div/p'

    # for drag and drop
    BASKET = By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]'

    # locators for modal info window
    MODAL_CLOSE_BUTTON = By.XPATH, '//section[contains(@class, "Modal_modal_opened")]/div/button[contains(@class, "Modal_modal__close_modified")]'
    TEXT_IN_MODAL_INGREDIENT_INFO = By.XPATH, '//*[text()="Детали ингредиента"]'
    CLOSE_MODAL_INFO_WINDOW = By.XPATH, '//div/section'

    # button to redirect to personal account
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, "//a[contains(@class, 'AppHeader_header__link') and @href='/account']"

    # button to redirect to list of orders
    LIST_OF_ORDERS_BUTTON = By.XPATH, '//*[text()="Лента Заказов"]'

    # button to redirect to kit page
    KIT_BUTTON = By.XPATH, '//*[text()="Конструктор"]'

    # button set order
    SET_ORDER = By.XPATH, '//*[text()="Оформить заказ"]'

    # text with order number
    ID_ORDER = By.XPATH, '//h2[contains(@class, "Modal_modal__title_shadow")]'
