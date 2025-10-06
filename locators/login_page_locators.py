from selenium.webdriver.common.by import By

class LoginPageLocators:
    # Поле ввода email на странице логина
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    
    # Поле ввода пароля на странице логина
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    
    # Кнопка "Войти" для авторизации
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    
    # Ссылка "Восстановить пароль" для перехода на страницу восстановления
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[contains(text(), 'Восстановить пароль')]")