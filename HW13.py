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
        time.sleep(10)
        numbers = driver.find_element_by_css_selector("#cart > a.content > span.quantity").get_attribute("textContent")

    # Go to cart
    driver.get("http://localhost/litecart/en/checkout")
    m = len(driver.find_elements_by_css_selector("#order_confirmation-wrapper > table > tbody td.item"))
    driver.find_element_by_css_selector("#box-checkout-cart > ul > li:nth-child(1) > a").click()  # stop karusel
    driver.find_element_by_name("remove_cart_item").click()

    for i in (1, m + 1):
        if len(driver.find_elements_by_css_selector("#order_confirmation-wrapper > table > tbody td.item")) != 0:
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div [id=checkout-cart-wrapper][style="opacity: 1;"]')))
            driver.find_element_by_name("remove_cart_item").click()

    a = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#checkout-cart-wrapper > p:nth-child(1) > em"))).get_attribute("textContent")
    assert a == "There are no items in your cart.", "Not deleted item(s)"
    time.sleep(20)

    # t1.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#box-checkout-cart > div > ul > li:nth-child(1) > form > div > p:nth-child(4) > button")))
    # driver.find_element_by_css_selector("#box-checkout-cart > div > ul > li:nth-child(1) > form > div > p:nth-child(4) > button").click()
    # f = driver.find_elements_by_css_selector("td.item").size()
    #  if WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_css_selector("td.item").is_displayed()):

  #      m = m - 1

        # driver.find_element_by_name("remove_cart_item").click()

 #    driver.find_element_by_css_selector("#box-checkout-cart > div > ul > li:nth-child(1) > form > div > p:nth-child(4) > button").click()
 #  #  time.sleep(30)
 #    driver.find_element_by_css_selector("#box-checkout-cart > div > ul > li:nth-child(1) > form > div > p:nth-child(4) > button").click()
 # #   time.sleep(30)
 #    driver.find_element_by_css_selector("#box-checkout-cart > div > ul > li:nth-child(1) > form > div > p:nth-child(4) > button").click()
 #      #  m = m - 1
 #    #

    # t3 = WebDriverWait(driver, 20)
    # a = t3.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#checkout-cart-wrapper > p:nth-child(1) > em"))).get_attribute("textContent")
    # assert a == "There are no items in your cart.", "Not sorted"
