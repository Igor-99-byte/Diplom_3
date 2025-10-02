from selenium.webdriver.common.by import By

class OrderFeedLocators:
    # Карточки заказов в ленте заказов
    ORDER_ITEMS = (By.XPATH, "//li[contains(@class, 'OrderHistory_listItem')]")
    
    # Модальное окно с деталями заказа
    ORDER_MODAL = (By.XPATH, "//li[1]//a[1]//div[2]")
    
    # Счетчик "Выполнено за все время" (число)
    TOTAL_ORDERS_COUNT = (By.XPATH, "//p[contains(text(), 'Выполнено за все время:')]/following-sibling::p")
    
    # Счетчик "Выполнено за сегодня" (число)
    TODAY_ORDERS_COUNT = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня:')]/following-sibling::p")
    
    # Номера заказов в разделе "В работе"
    IN_PROGRESS_ORDERS = (By.CSS_SELECTOR, "ul[class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi'] li[class='text text_type_digits-default mb-2']")