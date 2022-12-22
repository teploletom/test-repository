import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    numbers = 0
    while int(numbers) <= 2:
        driver.get("http://localhost/litecart/en/")
        driver.find_element_by_css_selector("#box-most-popular > div > ul > li:nth-child(1) > a.link").click()
        driver.find_element_by_name("add_cart_product").click()
      #  t = WebDriverWait(driver, 15)
      #  numbers = t.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#cart > a.content > span.quantity"))).get_attribute("textContent")
        time.sleep(10)
        numbers = driver.find_element_by_css_selector("#cart > a.content > span.quantity").get_attribute("textContent")
        print(numbers)

    # Go to cart
    driver.get("http://localhost/litecart/en/checkout")
    time.sleep(10)
    driver.find_element_by_css_selector("#box-checkout-cart > div > ul > li:nth-child(2)").click()
    m = len(driver.find_elements_by_css_selector("#order_confirmation-wrapper > table > tbody td.item"))
    print(m)
    while m >= 1:
        print(m)
        driver.find_element_by_name("remove_cart_item").click()
        m = m - 1
    t3 = WebDriverWait(driver, 20)
    a = t3.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#checkout-cart-wrapper > p:nth-child(1) > em"))).get_attribute("textContent")
    assert a == "There are no items in your cart.", "Not sorted"
