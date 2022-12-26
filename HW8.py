import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    m = len(driver.find_elements_by_css_selector("tr.row"))  # count of all elements
    list_country = []
    list1 = []

    for i in range(2, m + 2):
        country_name = (driver.find_elements(By.CSS_SELECTOR, f'#content > form > table > tbody > tr:nth-child({i}) > td:nth-child(5) > a'))
        for y in country_name:
            y = y.text
            list_country.append(y)
            zone = driver.find_elements(By.CSS_SELECTOR, f'#content > form > table > tbody > tr:nth-child({i}) > td:nth-child(6)')
            for j in zone:
                j = j.text
                if j != "0":
                    driver.find_element(By.CSS_SELECTOR, f'#content > form > table > tbody > tr:nth-child({i}) > td:nth-child(5) > a').click()
                    m1 = len(driver.find_elements_by_css_selector("#table-zones > tbody tr")) #count zones inside Country
                    for p in range(2, m1):
                        country_name1 = (driver.find_element(By.CSS_SELECTOR,
                                                             f'#table-zones > tbody > tr:nth-child({p}) > td:nth-child(3)'))
                        list1.append(country_name1.get_property('textContent'))
                    sorted_list1 = sorted(list1)
                    assert list1 == sorted_list1, "Not sorted"
                    list1 = []    #clean list
                    sorted_list1 = []
                    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    list_country1 = list_country
    assert list_country1 == list_country, "Not sorted"
