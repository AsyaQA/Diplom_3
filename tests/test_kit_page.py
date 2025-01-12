import pytest
import allure
from locators.kit_page_locators import KitPageLocators as KP, KitPageLocators
from pages.account_page import AccountPage
from pages.kit_page import KitPage
from pages.login_page import LoginPage


class TestKitPage:

    @allure.title('Проверка открытия и закрытия модалки с инфо об ингредиенте')
    @pytest.mark.parametrize(
        'locators',
        [
            KP.FLUORESCENT_BUN_R2_D3,
            KP.KRATORNAYA_BUN_N_200I,
            KP.SPICY_X_SAUCE,
            KP.SPACE_SAUCE,
            KP.TRADITIONAL_GALACTIC_SAUCE,
            KP.ANTARIAN_FLATWALKER_SAUCE,
            KP.PROTOSTOMIA_MEAT,
            KP.BEEF_CHOP,
            KP.BIO_CUTLET_MAGNOLIA,
            KP.FILLET_OF_LUMINESCENT,
            KP.CRISPY_RINGS,
            KP.FRUITS_OF_FALLENIAN_TREE,
            KP.MARTIAN_CRYSTALS,
            KP.MINI_SALAD,
            KP.BLUE_CHEESE
        ]
    )
    def test_open_and_closed_modal_info(self, driver, locators):
        kit_page = KitPage(driver)
        kit_page.open_ingredient_info(locators)
        kit_page.close_ingredient_info()
        assert 'Modal_modal_opened' not in kit_page.get_attribute_from_modal_info_window()

    @allure.title('Проверка перехода в конструктор из личного кабинета')
    def test_redirect_to_kit_page_from_account_page(self, driver):
        kit_page = KitPage(driver)
        account_page = AccountPage(driver)
        kit_page.click_to_personal_account()
        account_page.redirect_to_kit_page()
        assert kit_page.control_redirect_to_kit_page() == 'Краторная булка N-200i'

    @allure.title('Проверка изменения каунтера ингредиента при добавлении его в заказ')
    @pytest.mark.parametrize(
        'locators, counter',
        [
            (KP.FLUORESCENT_BUN_R2_D3, KP.FLUORESCENT_COUNTER),
            (KP.KRATORNAYA_BUN_N_200I, KP.KRATORNAYA_COUNTER),
            (KP.SPICY_X_SAUCE, KP.SPICY_X_SAUCE_COUNTER),
            (KP.SPACE_SAUCE, KP.SPACE_SAUCE_COUNTER),
            (KP.TRADITIONAL_GALACTIC_SAUCE, KP.TRADITIONAL_GALACTIC_SAUCE_COUNTER),
            (KP.ANTARIAN_FLATWALKER_SAUCE, KP.ANTARIAN_FLATWALKER_SAUCE_COUNTER),
            (KP.PROTOSTOMIA_MEAT, KP.PROTOSTOMIA_MEAT_COUNTER),
            (KP.BEEF_CHOP, KP.BEEF_CHOP_COUNTER),
            (KP.BIO_CUTLET_MAGNOLIA, KP.BIO_CUTLET_MAGNOLIA_COUNTER),
            (KP.FILLET_OF_LUMINESCENT, KP.FILLET_OF_LUMINESCENT_COUNTER),
            (KP.CRISPY_RINGS, KP.CRISPY_RINGS_COUNTER),
            (KP.FRUITS_OF_FALLENIAN_TREE, KP.FRUITS_OF_FALLENIAN_TREE_COUNTER),
            (KP.MARTIAN_CRYSTALS, KP.MARTIAN_CRYSTALS_COUNTER),
            (KP.MINI_SALAD, KP.MINI_SALAD_COUNTER),
            (KP.BLUE_CHEESE, KP.BLUE_CHEESE_COUNTER)
        ]
    )
    def test_counter_change_check(self, driver, locators, counter):
        kit_page = KitPage(driver)
        kit_page.drag_and_drop_ingredients(locators)
        assert kit_page.get_text_from_element(counter) != '0'

    @allure.title('Проверка создания заказа залогиненным пользователем')
    def test_create_order(self, driver):
        kit_page = KitPage(driver)
        login_page = LoginPage(driver)
        login_page.login_to_account()
        kit_page.set_order()
        assert kit_page.control_id_order() != '9999'
