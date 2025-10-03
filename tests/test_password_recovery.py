import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage

@allure.feature("Восстановление пароля")
class TestPasswordRecovery:
    @allure.title("Переход на страницу восстановления пароля")
    def test_navigate_to_password_recovery(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_personal_account()
        
        login_page = LoginPage(driver)
        login_page.click_forgot_password_link()
        
        login_page.wait_for_url_contains("forgot-password")

    @allure.title("Ввод почты и клик по кнопке 'Восстановить'")
    def test_password_recovery_with_email(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.get(forgot_password_page.base_url + "/forgot-password")
        forgot_password_page.enter_email("test@example.com")
        forgot_password_page.click_reset_button()
        
        forgot_password_page.wait_for_url_contains("reset-password")

    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным")
    def test_show_hide_password_highlights_field(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.get(forgot_password_page.base_url + "/forgot-password")
        
        forgot_password_page.click_reset_button()
        forgot_password_page.click_show_password_button()
        
        assert forgot_password_page.is_password_field_active()