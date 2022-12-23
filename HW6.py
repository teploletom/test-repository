import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    m = len(driver.find_elements(By.XPATH, '//*[@id="app-"]/a'))

    for i in range(1, m+1):
        driver.find_element(By.XPATH, f'//*[@id="box-apps-menu"]/li[{i}]/a').click()
        driver.find_element(By.TAG_NAME, 'h1').text

        x = len(driver.find_elements(By.CSS_SELECTOR, 'ul.docs li'))
        for j in range(1, x+1):
           driver.find_element(By.XPATH, f'//*[@id="app-"]/ul/li[{j}]/a').click()
           driver.find_element(By.TAG_NAME, 'h1').text
