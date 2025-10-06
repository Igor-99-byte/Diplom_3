from selenium.webdriver.common.by import By

class ProfilePageLocators:
    # Ссылка "История заказов" в личном кабинете
    ORDER_HISTORY_LINK = (By.XPATH, "//a[contains(text(),'История заказов')]")
    
    # Кнопка "Выход" для выхода из аккаунта
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")
    
    # Элементы заказов в истории заказов
    ORDER_ITEMS = (By.XPATH, "//div[contains(@class, 'OrderHistory_listItem')]")