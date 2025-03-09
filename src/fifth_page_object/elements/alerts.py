from selenium.webdriver.common.by import By
from src.fifth_page_object.elements.base_class import Base_class_page

class Home_page_alerts(Base_class_page):
    ALERT_SUCCESS = (By.CSS_SELECTOR, '#alert > div.alert-success')
    ALERT_BUTTON_CLOSE = (By.CSS_SELECTOR, '#alert > div > button.btn-close')

class Registration_page_alerts(Base_class_page):
    ALERT_MUST_AGREE_PRIVACY_POLICY = (By.CSS_SELECTOR, '#alert > dir.alert-danger')
