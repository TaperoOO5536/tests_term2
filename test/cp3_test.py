import pytest
from selenium import webdriver
from page_object.Home_page import HomePage
# from page_object.Product_page import ProductPage
# from page_object.Review_page import ReviewPage
from selenium.webdriver.common.by import By
from time import sleep

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def pages(driver):
  home_page = HomePage(driver)
  #  product_page = ProductPage(driver)
  #  review_page = ReviewPage(driver)
  #  return home_page, product_page, review_page
  return home_page

@pytest.fixture(autouse=True)
def setup(pages):
    home_page = pages
    home_page.navigate_to("http://localhost:8080")

def test_something(pages):
    home_page = pages
    home_page.search("iphone")
    sleep(1)
