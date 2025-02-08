from selenium.webdriver.common.by import By
from src.fifth_page_object.elements.base_class import Base_class_page

class Personal_page(Base_class_page):
    MY_ACCOUNT_HEADER = (By.CSS_SELECTOR, '#content > h2:nth-child(1)')