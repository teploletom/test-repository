import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


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
        m3 = len(driver.find_elements_by_css_selector("#table-zones > tbody > tr:nth-child(3) > td:nth-child(3) > select > option"))# count of Zone Edit Geo Zone page, ДРУГОГО РЕЛЕВАТНОГО ЛОКАТОРА НЕ НАШЛА
        for j in range(2, m2 + 2):
            for y in range(2, m3+1):
                a = driver.find_element_by_css_selector(f"#table-zones > tbody > tr:nth-child({j}) > td:nth-child(3) > select > option:nth-child({y})").get_attribute("selected")
                if a == 'true':
                    country_name = driver.find_elements_by_css_selector(
                        f"#table-zones > tbody > tr:nth-child({j}) > td:nth-child(3) > select > option:nth-child({y})") #save country
                    for x in country_name:
                        x = x.text
                        list.append(x)
        sorted_list = sorted(list)
        assert list == sorted_list, "Not sorted"
        driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")

