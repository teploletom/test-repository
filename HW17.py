import pytest
from selenium import webdriver
import time
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

d = DesiredCapabilities.EDGE
d['ms:loggingPrefs'] = { 'browser':'ALL' }


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    m = len(driver.find_elements(By.XPATH, "//td[3]/a[contains(@href, 'edit_product')]"))
    for i in range(4, m+5):
        driver.find_element(By.CSS_SELECTOR, f'#content > form > table > tbody > tr:nth-child({i}) > td:nth-child(3) > a').click()
        for l in driver.get_log("browser"):
            print(l)
        driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
