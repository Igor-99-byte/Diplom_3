from selenium.webdriver.common.by import By

class ForgotPasswordLocators:
    # Поле ввода email на странице восстановления пароля
    EMAIL_INPUT = (By.XPATH, "//input[contains(@name,'name')]")
    
    # Кнопка "Восстановить" для отправки запроса
    RESET_BUTTON = (By.XPATH, "//button[contains(text(),'Восстановить')]")
    
    # Иконка глаза для показа/скрытия пароля
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class, 'input_type_password')]//div[contains(@class, 'input__icon-action')]")
    
    # Активное поле пароля (подсвеченное после клика на глаз)
    ACTIVE_PASSWORD_FIELD = (By.XPATH, "//div[contains(@class, 'input_type_password') and contains(@class, 'input_status_active')]")
