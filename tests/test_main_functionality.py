import time
import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage

@allure.feature("Основной функционал")
class TestMainFunctionality:
    @allure.title("Переход по клику на 'Конструктор'")
    def test_navigate_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_constructor()
        
        assert driver.current_url == main_page.base_url + "/"

    @allure.title("Переход по клику на 'Лента заказов'")
    def test_navigate_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_order_feed()
        
        assert "feed" in driver.current_url

    @allure.title("Клик на ингредиент открывает всплывающее окно с деталями")
    def test_ingredient_modal_opening(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_ingredient()
        
        assert main_page.is_modal_visible()

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_ingredient_modal_closing(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_ingredient()
        main_page.close_modal()
        time.sleep(2)
        
        assert not main_page.is_modal_visible()

    @allure.title("При добавлении ингредиента в заказ увеличивается каунтер")
    def test_ingredient_counter_increase(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        
        initial_count = main_page.get_ingredient_counter()
        main_page.add_ingredients_to_order()
        new_count = main_page.get_ingredient_counter()
        
        assert new_count > initial_count

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_order_creation_by_logged_in_user(self, logged_in_user):
        driver, email, password, name, token = logged_in_user
        
        main_page = MainPage(driver)
        main_page.add_ingredients_to_order()
        main_page.click_order_button()
        time.sleep(2)
        
        assert main_page.is_order_modal_visible()