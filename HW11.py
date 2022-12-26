import pytest
from selenium import webdriver
from random import randint



@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://localhost/litecart/en/create_account")
    driver.find_element_by_name("company").send_keys("CMA")
    driver.find_element_by_name("firstname").send_keys("Yulia")
    driver.find_element_by_name("lastname").send_keys("Vas")
    driver.find_element_by_name("address1").send_keys("Street")
    driver.find_element_by_name("postcode").send_keys("11111")
    driver.find_element_by_name("city").send_keys("Moscow")
    driver.find_element_by_css_selector("span.select2-selection__arrow").click()
    driver.find_element_by_css_selector("input.select2-search__field").send_keys("United States""\n")
    random_num=str(randint(0, 9999999))
    driver.find_element_by_name("email").send_keys("Yulia" + random_num + "@gmail.com")
    email = "Yulia" + random_num + "@gmail.com"
    driver.find_element_by_name("phone").send_keys("+79169181816")
    driver.find_element_by_name("password").send_keys("111111")
    driver.find_element_by_name("confirmed_password").send_keys("111111")
    driver.find_element_by_name("create_account").click()
    driver.get("http://localhost/litecart/en/logout")
    driver.find_element_by_name("email").send_keys(f'{email}')
    driver.find_element_by_name("password").send_keys("111111")
    driver.find_element_by_name("login").click()
    driver.get("http://localhost/litecart/en/logout")


