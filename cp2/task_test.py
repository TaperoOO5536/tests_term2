import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_product_scrinshoots(driver):
    driver.get("http://localhost:8080")
    sleep(2)
    
    product_link = driver.find_element(By.XPATH, "//a[contains(text(), 'MacBook')]")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", product_link)
    sleep(0.2)
    product_link.click()
    sleep(1)
    first_img = driver.find_element(By.CSS_SELECTOR, "img[src$='macbook_3-74x74.jpg']")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", first_img)
    sleep(0.2)
    first_img.click()
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, '.mfp-arrow.mfp-arrow-right.mfp-prevent-close').click()
    sleep(1)
    assert  'macbook_2-800x800.jpg' in driver.find_element(By.CSS_SELECTOR, '.mfp-img').get_attribute("src"), 'something went wrong during changing image'


def test_change_currency(driver):
    driver.get("http://localhost:8080")
    sleep(2)

    driver.find_element(
        By.CSS_SELECTOR, 
        '.fa-solid.fa-caret-down').click()
    sleep(1)
    driver.find_element(
        By.XPATH, 
        "//a[contains(text(), '€ Euro')]").click()
    sleep(1)
    assert driver.find_element(By.CSS_SELECTOR, '.dropdown-toggle > strong').text == '€', 'Currency is still dollar'
    driver.find_element(
        By.CSS_SELECTOR, 
        '.fa-solid.fa-caret-down').click()
    sleep(1)
    driver.find_element(
        By.XPATH, 
        "//a[contains(text(), '$ US Dollar')]").click()
    sleep(1)
    assert driver.find_element(By.CSS_SELECTOR, '.dropdown-toggle > strong').text == '$', 'Currency is still euro'

def test_pc_categoty_is_empty(driver):
    driver.get("http://localhost:8080")
    sleep(2) 

    driver.find_element(
        By.XPATH, 
        "//a[contains(text(), 'Desktops')]").click()
    sleep(1)
    driver.find_element(
        By.XPATH, 
        "//a[contains(text(), 'PC (0)')]").click()
    sleep(1)
    assert len(driver.find_elements(By.XPATH, "//p[contains(text(), 'There are no products to list in this category.')]")) != 0, 'PC list is not empty'

def test_registration(driver):
    driver.get("http://localhost:8080")
    sleep(2)

    driver.find_element(
        By.XPATH, 
        "//span[contains(text(), 'My Account')]").click()
    sleep(1)
    driver.find_element(
        By.XPATH, 
        "//a[contains(text(), 'Register')]").click()
    sleep(1)
    driver.find_element(
        By.CSS_SELECTOR, 
        "#input-firstname").send_keys("Firstname")
    sleep(1)
    driver.find_element(
        By.CSS_SELECTOR, 
        "#input-lastname").send_keys("Lastname")
    sleep(1)
    driver.find_element(
        By.CSS_SELECTOR, 
        "#input-email").send_keys("asd@asd.ru")
    sleep(1)
    driver.find_element(
        By.CSS_SELECTOR, 
        "#input-password").send_keys("qwerty")
    sleep(1)
    driver.find_element(By.NAME, "agree").click()
    sleep(1)
    driver.find_element(
        By.XPATH, 
        "//button[contains(text(), 'Continue')]").click()
    sleep(3)
    assert len(driver.find_elements(By.XPATH, "//h1[contains(text(), 'Your Account Has Been Created!')]")) != 0, 'Registration faild for some reason'

def test_search(driver):
    driver.get("http://localhost:8080")
    sleep(2)

    driver.find_element(
        By.NAME, "search").send_keys('asdf')
    sleep(1)
    driver.find_element(
        By.CSS_SELECTOR, '.btn.btn-light.btn-lg').click()
    sleep(1)
    assert (len(driver.find_elements(By.CSS_SELECTOR, "#product-list")) != 0) or len(driver.find_elements(By.XPATH, "//p[contains(text(), 'There is no product that matches the search criteria.')]")) != 0, 'Something went wrong('
