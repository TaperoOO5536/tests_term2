from selenium.webdriver.common.by import By

def test_add_to_wish_list(pages):
    home_page, _, _, login_page = pages
    # login_page.go_to_signup_page()
    # login_page.signup("Test", "User", "asd@asd.ru", "qweasz1234")
    login_page.go_to_login_page()
    login_page.login("asd@asd.ru", "qweasz1234")
    home_page.go_to_home()
    home_page.add_to_wish_list_from_home("MacBook", 400)
    home_page.close_alert()
    home_page.go_to_wish_list()
    assert len(home_page.driver.find_elements(By.XPATH, "//td//a[contains(text(), 'MacBook')]")) != 0, "MacBook was not added to the wish list."

def test_add_camera_to_cart(pages):
    home_page, product_page, cart_page, _ = pages
    home_page.go_to_home()
    product_page.go_to_product_page("Canon EOS 5D", 700)
    product_page.choose_color("Red")
    product_page.add_to_cart()
    product_page.close_alert()
    home_page.go_to_cart()
    assert len(home_page.driver.find_elements(By.XPATH, "//td//a[contains(text(), 'Canon EOS 5D')]")) != 0, "Canon EOS 5D was not added to the cart."

def test_add_tablet_to_cart(pages):
    home_page, product_page, _, _ = pages
    home_page.go_to_category("tablet")
    product_page.go_to_product_page("Samsung Galaxy Tab 10.1")
    product_page.add_to_cart()
    product_page.close_alert()
    home_page.go_to_cart()
    assert len(home_page.driver.find_elements(By.XPATH, "//td//a[contains(text(), 'Samsung Galaxy Tab 10.1')]")) != 0, "Samsung Galaxy Tab 10.1 was not added to the cart."

def test_add_htc_phone_to_cart(pages):
    home_page, product_page, _, _ = pages
    home_page.go_to_category("smartphone")
    product_page.go_to_product_page("HTC Touch HD")
    product_page.add_to_cart()
    product_page.close_alert()
    home_page.go_to_cart()
    assert len(home_page.driver.find_elements(By.XPATH, "//td//a[contains(text(), 'HTC Touch HD')]")) != 0, "HTC Touch HD was not added to the cart."

def test_write_review(pages):
    home_page, product_page, _, _ = pages
    home_page.search("iPhone")
    product_page.go_to_product_page("iPhone", 200)
    product_page.write_review("This is a great phone!", 5)
