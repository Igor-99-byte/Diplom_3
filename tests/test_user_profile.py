import allure
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
import time

@allure.feature("Личный кабинет")
class TestUserProfile:
    @allure.title("Переход по клику на 'Личный кабинет'")
    def test_navigate_to_personal_account(self, logged_in_user):
        driver, email, password, name, token = logged_in_user

        main_page = MainPage(driver)

        main_page.click_personal_account()
        time.sleep(2)
        
        assert "account" in driver.current_url

    @allure.title("Переход в раздел 'История заказов'")
    def test_navigate_to_order_history(self, logged_in_user):
        driver, email, password, name, token = logged_in_user

        main_page = MainPage(driver)

        main_page.click_personal_account()
        
        profile_page = ProfilePage(driver)
        profile_page.click_order_history_link()
        
        assert "order-history" in driver.current_url

    @allure.title("Выход из аккаунта")
    def test_logout(self, logged_in_user):
        driver, email, password, name, token = logged_in_user

        main_page = MainPage(driver)

        main_page.click_personal_account()
        
        profile_page = ProfilePage(driver)
        profile_page.click_logout_button()
        time.sleep(2)
        
        assert "login" in driver.current_url