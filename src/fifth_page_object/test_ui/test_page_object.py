import random
import allure
from src.fifth_page_object.elements.common_elements import Common_elements
from src.fifth_page_object.elements.home_page import Home_page, Product_card
from src.fifth_page_object.elements.login_form import Login_form
from src.fifth_page_object.elements.personal_page import Personal_page
from src.fifth_page_object.elements.registration import Registration_page
from src.fifth_page_object.elements.alerts import Registration_page_alerts


@allure.title('Тест основных элементов разных страниц')
def test_common_elem_on_different_pages(base_url, browser, set_currencies, paths, get_phone):
    cmn_elements = Common_elements(browser, base_url)
    cmn_elements.change_path(paths)
    cmn_elements.open_page()
    cmn_elements.currencies_dropdown_click()
    currencies = cmn_elements.check_visibility_some_elements(cmn_elements.CURRENCIES)
    with allure.step(f'Проверяем {len(currencies)} и {len(set_currencies)}'):
        assert len(currencies) == len(set_currencies)
    inline_items = cmn_elements.check_visibility_some_elements(cmn_elements.INLINE_ITEMS)
    with allure.step(f'Проверяем {len(inline_items)} и 5'):
        assert len(inline_items) == 5
    cmn_elements.my_account_click()
    register_login_items = cmn_elements.check_visibility_some_elements(cmn_elements.ITEMS_LOGIN_REGISTER)
    with allure.step(f'Сравниваем  {len(register_login_items)} и 2'):
        assert len(register_login_items) == 2
    register, login = register_login_items
    with allure.step(f' Сравниваем {register.get_attribute("href")} и f"{base_url}/en-gb?route=account/register"'):
        assert register.get_attribute('href') == f'{base_url}/en-gb?route=account/register'
    with allure.step(f'Сравниваем {login.get_attribute("href")}'):
        assert login.get_attribute('href') == f'{base_url}/en-gb?route=account/login'
    cmn_elements.my_account_click()
    wishlist = cmn_elements.check_visibility_of_element(cmn_elements.WISHLIST_URL)
    with allure.step(f'wishlist.get_attribute("href") и {base_url}/en-gb?route=account/wishlist'):
        assert wishlist.get_attribute('href') == f'{base_url}/en-gb?route=account/wishlist'
    with allure.step(f'Сравниваем {wishlist.get_attribute("title")} с Wish List (0)'):
        assert wishlist.get_attribute('title') == 'Wish List (0)'
    phone_elem = cmn_elements.check_visibility_of_element(cmn_elements.PHONE_NUMBER)
    with allure.step(f'Сравниваем {phone_elem.text} с {get_phone}'):
        assert phone_elem.text == get_phone
    with allure.step(f'Сравниваем {cmn_elements.check_visibility_of_element(cmn_elements.SHOPPING_CART)} с {inline_items[3]}'):
        assert cmn_elements.check_visibility_of_element(cmn_elements.SHOPPING_CART) == inline_items[3]
    shopping_cart_url = cmn_elements.check_visibility_of_element(cmn_elements.SHOPPING_CART_URL)
    shopping_cart_text = cmn_elements.check_visibility_of_element(cmn_elements.SHOPPING_CART_TEXT)
    with allure.step(f'Сравниваем {shopping_cart_url.get_attribute("href")} и {base_url}/en-gb?route=checkout/cart'):
        assert shopping_cart_url.get_attribute('href') == f'{base_url}/en-gb?route=checkout/cart'
    with allure.step(f'Сравниваем {shopping_cart_text.text} и Shopping Cart'):
        assert shopping_cart_text.text == 'Shopping Cart'
    checkout_url = cmn_elements.check_visibility_of_element(cmn_elements.CHECKOUT_URL)
    checkout_text = cmn_elements.check_visibility_of_element(cmn_elements.CHECKOUT_TEXT)
    with allure.step(f'Сравниваем {checkout_url.get_attribute("href")} и {base_url}/en-gb?route=checkout/checkout'):
        assert checkout_url.get_attribute('href') == f'{base_url}/en-gb?route=checkout/checkout'
    with allure.step(f'{checkout_text.text} и Checkout'):
        assert checkout_text.text == 'Checkout'
    with allure.step(f'Проверка видимости {cmn_elements.check_visibility_of_element(cmn_elements.LOGO)}'):
        assert cmn_elements.check_visibility_of_element(cmn_elements.LOGO)
    search_field = cmn_elements.check_visibility_of_element(cmn_elements.SEARCH_FIELD)
    with allure.step(f'Сравниваем {search_field.get_attribute("type")} и text'):
        assert search_field.get_attribute('type') == 'text'
    search_button = cmn_elements.check_visibility_of_element(cmn_elements.SEARCH_BTN)
    with allure.step(f'Сравниваем {search_button.get_attribute("type")} и button'):
        assert search_button.get_attribute('type') == 'button'
    cmn_elements.input_in_search_field('This is test input')
    cmn_elements.click_elem(cmn_elements.SEARCH_BTN)
    with allure.step(f'Сравниваем что {cmn_elements.browser.current_url} не равен {base_url}{paths}'):
        assert cmn_elements.browser.current_url != f'{base_url}{paths}'


@allure.title('Тест изменения валют на основной странице')
def test_change_currency_in_home_page(base_url, browser, set_currencies, curns):
    cmn_elements = Common_elements(browser, base_url)
    cur_name, cur_symb = curns
    cmn_elements.open_page()
    cmn_elements.currencies_dropdown_click()
    cmn_elements.change_currency(cur_name)
    list_products = Home_page(browser, base_url)
    list_products.check_visibility_of_element(list_products.LIST_PRODUCTS)
    products = Product_card(browser, base_url)
    lst_prices_new = products.check_visibility_some_elements(products.PRICE_NEW)
    for new_price in lst_prices_new:
        with allure.step(f'Проверяем вхождение {cur_symb} в {new_price.text}'):
            assert cur_symb in new_price.text
    lst_prices_tax = products.check_visibility_some_elements(products.PRICE_TAX)
    for price_tax in lst_prices_tax:
        with allure.step(f'Вхождение {cur_symb} в {price_tax.text}'):
            assert cur_symb in price_tax.text


@allure.title('Тест добавления товара в корзину')
def test_product_add_to_cart(base_url, browser):
    home_page = Home_page(browser, base_url)
    home_page.open_page()
    home_page.check_visibility_of_element(home_page.LIST_PRODUCTS, 5)
    product_items_pick = home_page.check_visibility_of_element(home_page.PRODUCT_ITEMS_PICK)
    with allure.step(f'Сравниваем {product_items_pick.text} и 0 item(s) - $0.00'):
        assert product_items_pick.text == '0 item(s) - $0.00'
    home_page.click_elem(home_page.PRODUCT_ITEMS_PICK)
    lst_add_to_cart = home_page.check_visibility_some_elements(home_page.LIST_PRDCT_EMPTY_ITEM)
    with allure.step(f'{len(lst_add_to_cart)} и 1'):
        assert len(lst_add_to_cart) == 1
    with allure.step(f'Сравниваем {lst_add_to_cart[0].text} и Your shopping cart is empty!'):
        assert lst_add_to_cart[0].text == 'Your shopping cart is empty!'
    home_page.click_elem(home_page.PRODUCT_ITEMS_PICK)
    products = Product_card(browser, base_url)
    lst_products = products.check_visibility_some_elements(products.PRODUCT_CARD)
    with allure.step(f'{len(lst_products)} и 4'):
        assert len(lst_products) == 4
    product_info = products.get_info_about_product(0)
    price_new = product_info.get("price_new")
    products.add_to_cart_nth_product(0)
    browser.refresh()
    product_items_pick_new = home_page.check_visibility_of_element(home_page.PRODUCT_ITEMS_PICK, 5)
    home_page.actions.move_to_element(product_items_pick_new).perform()
    with allure.step(f'{product_items_pick_new.text}== 1 item(s) - {price_new}'):
        assert product_items_pick_new.text == f'1 item(s) - {price_new}'
    home_page.click_elem(home_page.PRODUCT_ITEMS_PICK)
    product_list = home_page.get_info_about_product_in_cart()
    with allure.step(f'Сравниваем {len(product_list)} и 1'):
        assert len(product_list) == 1
    first_item = product_list[0]
    with allure.step(f'Сравниваем {first_item["name"]} и {product_info["product_name"]}'):
        assert first_item['name'] == product_info['product_name']
    with allure.step(f'Сравниваем {first_item["price"]} и {product_info["price_new"]}'):
        assert first_item['price'] == product_info['price_new']


@allure.title('Тест авторизации пользователя')
def test_login_user(base_url, browser, create_random_user):
    cmn_elem = Common_elements(browser, base_url)
    cmn_elem.open_page()
    email, password = create_random_user
    cmn_elem.my_account_click()
    cmn_elem.click_elem(cmn_elem.LOGIN_URL)
    personal_page = Personal_page(browser, base_url)
    login_page = Login_form(browser, base_url)
    login_page.click_elem(login_page.LOGIN_BUTTON)
    personal_page.wait_invisibility_element(personal_page.MY_ACCOUNT_HEADER)
    login_page.input_in_field(login_page.EMAIL_INPUT, email)
    login_page.click_elem(login_page.LOGIN_BUTTON)
    personal_page.wait_invisibility_element(personal_page.MY_ACCOUNT_HEADER)
    login_page.clear_field(login_page.EMAIL_INPUT)
    login_page.input_in_field(login_page.PASSWORD_INPUT, password)
    login_page.click_elem(login_page.LOGIN_BUTTON)
    personal_page.wait_invisibility_element(personal_page.MY_ACCOUNT_HEADER)
    login_page.clear_field(login_page.PASSWORD_INPUT)
    login_page.input_in_field(login_page.EMAIL_INPUT, email)
    login_page.input_in_field(login_page.PASSWORD_INPUT, password)
    login_page.click_elem(login_page.LOGIN_BUTTON)
    personal_page.check_visibility_of_element(personal_page.MY_ACCOUNT_HEADER)
    with allure.step(f'Сравниваем account/account&customer_token и {login_page.browser.current_url}'):
        assert 'account/account&customer_token' in login_page.browser.current_url
    cmn_elem.my_account_click()
    my_account_url = cmn_elem.check_visibility_of_element(cmn_elem.MY_ACCOUNT_URL)
    with allure.step(f'Сравниваем {my_account_url.text} и My Account'):
        assert my_account_url.text == 'My Account'
    order_history = cmn_elem.check_visibility_of_element(cmn_elem.ORDER_HISTORY)
    with allure.step(f'Сравниваем {order_history.text} и Order History'):
        assert order_history.text == 'Order History'
    transactions = cmn_elem.check_visibility_of_element(cmn_elem.TRANSACTIONS)
    with allure.step(f'Сравниваем {transactions.text} и Transactions'):
        assert transactions.text == 'Transactions'
    downloads = cmn_elem.check_visibility_of_element(cmn_elem.MY_ACCOUNT_DOWNLOADS)
    with allure.step(f'{downloads.text} и Downloads'):
        assert downloads.text == 'Downloads'
    logout = cmn_elem.check_visibility_of_element(cmn_elem.LOGOUT_URL)
    with allure.step(f'Сравниваем {logout.text} и Logout'):
        assert logout.text == 'Logout'
    cmn_elem.click_elem(cmn_elem.LOGOUT_URL)


@allure.title('Тест добавления товара в избранное без авторизации')
def test_add_to_wishlist_without_login(base_url, browser):
    home_page = Home_page(browser, base_url)
    home_page.open_page()
    products = Product_card(browser, base_url)
    lst_products = products.check_visibility_some_elements(products.PRODUCT_CARD, 5)
    with allure.step(f'Сравниваем {len(lst_products)} и 4'):
        assert len(lst_products) == 4
    rand_num = random.randint(1, len(lst_products) - 1)
    products.add_to_wishlist_nth_product(rand_num)
    cmn_elem = Common_elements(browser, base_url)
    wishlist = cmn_elem.check_visibility_of_element(cmn_elem.WISHLIST_TEXT, timeout=5)
    with allure.step(f'Сравниваем {wishlist.text} и Wish List (0)'):
        assert wishlist.text == 'Wish List (0)'


@allure.title('Тест изменения товаров в карусели товаров')
def test_change_slide_in_carousel(base_url, browser):
    home_page = Home_page(browser, base_url)
    home_page.open_page()
    carousel_items = home_page.check_presence_some_elements(home_page.CAROUSEL_ITEM, 5)
    with allure.step(f'Сравниваем {len(carousel_items)} и 2'):
        assert len(carousel_items) == 2
    home_page.check_visibility_of_element(home_page.FIRST_CAROUSEL_ITEM)
    home_page.check_visibility_of_element(home_page.SECOND_CAROUSEL_ITEM, 6)
    home_page.wait_invisibility_element(home_page.FIRST_CAROUSEL_ITEM)


@allure.title('Тест изменения слайдов карусели партнеров')
def test_change_slide_in_carousel_banner(base_url, browser):
    home_page = Home_page(browser, base_url)
    home_page.open_page()
    carousel_items = home_page.check_presence_some_elements(home_page.CAROUSEL_BANNER_ITEM, 5)
    with allure.step(f'Сравниваем {len(carousel_items)} и 3'):
        assert len(carousel_items) == 3
    home_page.check_visibility_of_element(home_page.FIRST_BANNER_ITEM)
    home_page.wait_invisibility_element(home_page.SECOND_BANNER_ITEM)
    home_page.wait_invisibility_element(home_page.THIRD_BANNER_ITEM)
    home_page.check_visibility_of_element(home_page.SECOND_BANNER_ITEM, 6)
    home_page.wait_invisibility_element(home_page.FIRST_BANNER_ITEM)
    home_page.wait_invisibility_element(home_page.THIRD_BANNER_ITEM)
    home_page.check_visibility_of_element(home_page.THIRD_BANNER_ITEM, 6)
    home_page.wait_invisibility_element(home_page.FIRST_BANNER_ITEM)
    home_page.wait_invisibility_element(home_page.SECOND_BANNER_ITEM)


@allure.title('Тест полей страницы авторизации и наличия предупреждений при отсутствии заполнения полей')
def test_fields_of_registration_page(base_url, browser):
    cmn_elem = Common_elements(browser, base_url)
    cmn_elem.open_page()
    cmn_elem.my_account_click()
    cmn_elem.check_visibility_of_element(cmn_elem.REGISTRATION_URL).click()
    cmn_elem.title_wait('Register Account')
    registration_page = Registration_page(browser, base_url)
    header_of_page = registration_page.check_visibility_of_element(registration_page.HEADER)
    personal_details = registration_page.check_visibility_of_element(registration_page.PERSONAL_DETAILS_LEGEND)
    with allure.step(f'Сравниваем {personal_details} и Your Personal Details'):
        assert personal_details.text == 'Your Personal Details'
    with allure.step(f'Сравниваем {header_of_page.text} и Register Account'):
        assert header_of_page.text == 'Register Account'
    first_name_label = registration_page.check_visibility_of_element(registration_page.FIRST_NAME_LABEL)
    with allure.step(f'Сравниваем {first_name_label.text} и First Name'):
        assert first_name_label.text == 'First Name'
    first_name_input = registration_page.check_visibility_of_element(registration_page.FIRST_NAME_INPUT)
    with allure.step(f'Сравниваем {first_name_input.get_attribute("type")} и text'):
        assert first_name_input.get_attribute('type') == 'text'
    with allure.step(f'{first_name_input.get_attribute("value")} с пустой строкой'):
        assert first_name_input.get_attribute('value') == ''
    with allure.step(f'{first_name_input.get_attribute("placeholder")} и First Name'):
        assert first_name_input.get_attribute('placeholder') == 'First Name'
    registration_page.wait_invisibility_element(registration_page.ERROR_FIRST_NAME)
    last_name_label = registration_page.check_visibility_of_element(registration_page.LAST_NAME_LABEL)
    with allure.step(f'Сравниваем {last_name_label.text} и Last Name'):
        assert last_name_label.text == 'Last Name'
    last_name_input = registration_page.check_visibility_of_element(registration_page.LAST_NAME_INPUT)
    with allure.step(f'{last_name_input.get_attribute("type")} и text'):
        assert last_name_input.get_attribute('type') == 'text'
    with allure.step(f'Сравниваем {last_name_input.get_attribute("value")} с пустой строкой'):
        assert last_name_input.get_attribute('value') == ''
    with allure.step(f'Сравниваем {last_name_input.get_attribute("placeholder")} и Last Name'):
        assert last_name_input.get_attribute('placeholder') == 'Last Name'
    registration_page.wait_invisibility_element(registration_page.ERROR_LAST_NAME)
    email_label = registration_page.check_visibility_of_element(registration_page.EMAIL_LABEL)
    with allure.step(f'Сравниваем {email_label.text} и E-Mail'):
        assert email_label.text == 'E-Mail'
    email_input = registration_page.check_visibility_of_element(registration_page.EMAIL_INPUT)
    with allure.step(f'{email_input.get_attribute("type")} и email'):
        assert email_input.get_attribute('type') == 'email'
    with allure.step(f'{email_input.get_attribute("value")} и E-Mail'):
        assert email_input.get_attribute('value') == ''
    with allure.step(f'{email_input.get_attribute("placeholder")} и E-Mail'):
        assert email_input.get_attribute('placeholder') == 'E-Mail'
    registration_page.wait_invisibility_element(registration_page.ERROR_EMAIL)
    password_details = registration_page.check_visibility_of_element(registration_page.PASSWORD_LEGEND)
    with allure.step(f'Сравниваем {password_details.text} и Your Password'):
        assert password_details.text == 'Your Password'
    password_input = registration_page.check_visibility_of_element(registration_page.PASSWORD_INPUT)
    with allure.step(f'Сравниваем {password_input.get_attribute("type")} и password'):
        assert password_input.get_attribute('type') == 'password'
    with allure.step(f'Сравниваем {password_input.get_attribute("value")} с пустой строкой'):
        assert password_input.get_attribute('value') == ''
    with allure.step(f'Сравниваем {password_input.get_attribute("placeholder")} и Password'):
        assert password_input.get_attribute('placeholder') == 'Password'
    registration_page.wait_invisibility_element(registration_page.ERROR_PASSWORD)
    newsletter = registration_page.check_visibility_of_element(registration_page.NEWLETTER_LEGEND)
    with allure.step(f'Сравниваем {newsletter.text} и Newsletter'):
        assert newsletter.text == 'Newsletter'
    subscribe_label = registration_page.check_visibility_of_element(registration_page.SUBSCRIBE_LABEL)
    with allure.step(f'Сравниваем {subscribe_label.text} и Subscribe'):
        assert subscribe_label.text == 'Subscribe'
    subscribe_switch = registration_page.check_visibility_of_element(registration_page.SUBSCRIBE_SWITCH)
    with allure.step(f'Сравниваем {subscribe_switch.get_attribute("type")} и checkbox'):
        assert subscribe_switch.get_attribute('type') == 'checkbox'
    policy_label = registration_page.check_visibility_of_element(registration_page.POLICY_LABEL)
    with allure.step(f'Сравниваем {policy_label.text} и I have read and agree to the Privacy Policy'):
        assert policy_label.text == 'I have read and agree to the Privacy Policy'
    continue_btn = registration_page.check_visibility_of_element(registration_page.CONTINUE_BTN)
    with allure.step(f'Сравниваем {continue_btn.text} и Continue'):
        assert continue_btn.text == 'Continue'
    url_before = browser.current_url
    continue_btn.click()
    error_first_name = registration_page.check_visibility_of_element(registration_page.ERROR_FIRST_NAME)
    with allure.step(f'Сравниваем {error_first_name.text} и First Name must be between 1 and 32 characters!'):
        assert error_first_name.text == 'First Name must be between 1 and 32 characters!'
    error_last_name = registration_page.check_visibility_of_element(registration_page.ERROR_LAST_NAME)
    with allure.step(f'Сравниваем {error_last_name.text} и Last Name must be between 1 and 32 characters!'):
        assert error_last_name.text == 'Last Name must be between 1 and 32 characters!'
    error_email = registration_page.check_visibility_of_element(registration_page.ERROR_EMAIL)
    with allure.step(f'Сравниваем {error_email.text} и E-Mail Address does not appear to be valid!'):
        assert error_email.text == 'E-Mail Address does not appear to be valid!'
    error_password = registration_page.check_visibility_of_element(registration_page.ERROR_PASSWORD)
    with allure.step(f'Сравниваем {error_password.text} и Password must be between 4 and 20 characters!'):
        assert error_password.text == 'Password must be between 4 and 20 characters!'
    url_after = browser.current_url
    with allure.step(f'Сравниваем {url_after} и {url_before}'):
        assert url_after == url_before


@allure.title('Регистрация пользователя с валидными данными')
def test_registration_with_valid_data(base_url, browser, create_valid_data_for_registration):
    registration = Registration_page(browser, base_url)
    registration.open_page()
    alerts = Registration_page_alerts(browser, base_url)
    registration.check_visibility_of_element(registration.FIRST_NAME_INPUT, 3)
    registration.input_in_field(registration.FIRST_NAME_INPUT, create_valid_data_for_registration['firstname'])
    registration.input_in_field(registration.LAST_NAME_INPUT, create_valid_data_for_registration['lastname'])
    registration.input_in_field(registration.EMAIL_INPUT, create_valid_data_for_registration['email'])
    registration.input_in_field(registration.PASSWORD_INPUT, create_valid_data_for_registration['password'])
    registration.click_elem(registration.CONTINUE_BTN)
    alert = alerts.check_visibility_of_element(alerts.ALERT_MUST_AGREE_PRIVACY_POLICY)
    with allure.step(f'Сравниваем {alert.text} и Warning: You must agree to the Privacy Policy!'):
        assert alert.text == 'Warning: You must agree to the Privacy Policy!'
    registration.click_elem(registration.POLICY_SWITCH)
    registration.click_elem(registration.CONTINUE_BTN)
