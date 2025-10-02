import pytest
import time
import allure
from pages.order_feed_page import OrderFeedPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.login_page import LoginPage

@allure.feature("Лента заказов")
class TestOrderFeed:
    @allure.title("Клик на заказ открывает всплывающее окно с деталями")
    def test_order_modal_opening(self, driver):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.driver.get(order_feed_page.base_url + "/feed")
        
        if order_feed_page.get_order_count() > 0:
            order_feed_page.click_order()
            assert order_feed_page.is_order_modal_visible()
        else:
            pytest.fail("Нет заказов для тестирования модального окна")

    @allure.title("Заказы пользователя из 'Истории заказов' отображаются в 'Ленте заказов'")
    def test_user_orders_in_feed(self, logged_in_user):
        driver, email, password, name, token = logged_in_user
        time.sleep(1)
        
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_personal_account()
        
        profile_page = ProfilePage(driver)
        profile_page.click_order_history_link()
        
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.driver.get(order_feed_page.base_url + "/feed")
        feed_orders_count = order_feed_page.get_order_count()
        
        assert feed_orders_count > 0

    @allure.title("При создании нового заказа счётчик 'Выполнено за всё время' увеличивается")
    def test_total_orders_counter_increase(self, logged_in_user):
        driver, email, password, name, token = logged_in_user
        time.sleep(1)

        order_feed_page = OrderFeedPage(driver)
        order_feed_page.driver.get(order_feed_page.base_url + "/feed")
        initial_total = order_feed_page.get_total_orders_count()
        
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.add_ingredients_to_order()
        main_page.click_order_button()
        assert main_page.is_order_modal_visible()
        
        order_feed_page.driver.get(order_feed_page.base_url + "/feed")
        new_total = order_feed_page.get_total_orders_count()
        time.sleep(2)
        
        assert new_total > initial_total

    @allure.title("При создании нового заказа счётчик 'Выполнено за сегодня' увеличивается")
    def test_today_orders_counter_increase(self, logged_in_user):
        driver, email, password, name, token = logged_in_user
        time.sleep(1)

        order_feed_page = OrderFeedPage(driver)
        order_feed_page.driver.get(order_feed_page.base_url + "/feed")
        initial_today = order_feed_page.get_today_orders_count()
        
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.add_ingredients_to_order()
        main_page.click_order_button()
        assert main_page.is_order_modal_visible()
        
        order_feed_page.driver.get(order_feed_page.base_url + "/feed")
        new_today = order_feed_page.get_today_orders_count()
        
        assert new_today > initial_today

    @allure.title("После оформления заказа его номер появляется в разделе 'В работе'")
    def test_order_in_progress_section(self, driver, logged_in_user):
        driver, email, password, name, token = logged_in_user
        time.sleep(1)

        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.add_ingredients_to_order()
        main_page.click_order_button()
        
        # Получаем динамический номер заказа
        order_number = main_page.get_order_number()
        time.sleep(2)
        assert order_number
        
        main_page.close_modal()
        
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.driver.get(order_feed_page.base_url + "/feed")
        in_progress_orders = order_feed_page.get_in_progress_orders()
        time.sleep(5)
        
        # Проверяем, что номер заказа есть в разделе "В работе"
        assert f'0{order_number}' in in_progress_orders