import pytest
import allure
from selenium import webdriver
import json
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", choices=["chrome", "firefox"])
    parser.addoption("--headless", action="store_true")
    parser.addoption("--executor", action="store", default="127.0.0.1:4444")
    parser.addoption("--log_level", action="store", default="INFO")

@pytest.fixture(scope="module")
def driver(request):
    browser_name = request.config.getoption("--browser")

# for selenoid
#     options = Options()
#     options.set_capability("browserName", "chrome")
#     options.set_capability("browserVersion", "latest")
#     options.set_capability("selenoid:options", {
#     "enableVNC": True,
#     "enableVideo": True,
#     "enableLog": True
# })

#     driver = webdriver.Remote(
#         command_executor="http://localhost:4444/wd/hub",
#         options=options
#     )

    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        raise NotImplementedError(f"Browser {browser_name} is not implemented.")
    driver.get("http://localhost:8080")

    allure.attach(
        name=driver.session_id,
        body=json.dumps(driver.capabilities),
        attachment_type=allure.attachment_type.JSON,
    )

    yield driver
    driver.quit()

@pytest.fixture
def pages(driver):
    from page_object.Home_page import HomePage
    from page_object.Product_page import ProductPage
    from page_object.Cart_page import CartPage
    from page_object.Login_page import LoginPage
    from page_object.Admin_page import AdminPage

    home_page = HomePage(driver)
    product_page = ProductPage(driver)
    cart_page = CartPage(driver)
    login_page = LoginPage(driver)
    admin_page = AdminPage(driver)
    return home_page, product_page, cart_page, login_page, admin_page

@pytest.fixture(scope="function")
def page(request):
    return request.param

@pytest.fixture(autouse=True)
def setup(pages, page):
    home_page, _, _, _, admin_page = pages

# for selenoid
    # if page == "admin":
    #     admin_page.navigate_to("http://host.docker.internal:8080/administration/")
    #     admin_page.login()
    # elif page == "home":
    #     home_page.navigate_to("http://host.docker.internal:8080")

    if page == "admin":
        admin_page.navigate_to("http://localhost:8080/administration/")
        admin_page.login()
    elif page == "home":
        home_page.navigate_to("http://localhost:8080")