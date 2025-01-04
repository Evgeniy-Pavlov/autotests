from selenium.webdriver.common.by import By
from src.fifth_page_object.elements.base_class import Base_class_page

class Home_page_alerts(Base_class_page):
    ADD_TO_CART = (By.CSS_SELECTOR, '#alert > div')
    ALERT_SUCCESS = (By.CSS_SELECTOR, '#alert > div.alert-success')
    ALERT_BUTTON_CLOSE = (By.CSS_SELECTOR, '#alert > div > button.btn-close')
