import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    m = len(driver.find_elements_by_css_selector("tr.row"))  # count of all elements -> 2
    list = []
    sorted_list = []

    for i in range(2, m + 2):
        driver.find_element(By.CSS_SELECTOR, f'#content > form > table > tbody > tr:nth-child({i}) > td:nth-child(5) > a').click()
        m2 = len(driver.find_elements_by_css_selector("span.select2-selection__rendered")) # count of all elements Edit Geo Zone page
        m3 = len(driver.find_elements_by_css_selector("#table-zones > tbody > tr:nth-child(3) > td:nth-child(3) > select > option"))# count of Zone Edit Geo Zone page
        for j in range(2, m2 + 2):
            select_element = driver.find_elements_by_css_selector(f"#table-zones > tbody > tr:nth-child({j}) > td:nth-child(3) > select option[selected]")
            for x in select_element:
                x = x.text
                list.append(x)
        sorted_list = sorted(list)
        assert list == sorted_list, "Not sorted"
        print(list)
        list = []  # clean list
        sorted_list = []
        driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")

