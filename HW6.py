import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
        a = driver.find_element(By.XPATH,
                                f'/html/body/div/div/div/table/tbody/tr/td[1]/div[3]/ul/li[{i}]/a/span[2]').click()
        driver.find_element(By.TAG_NAME, 'h1').text
        x = len(driver.find_elements(By.CSS_SELECTOR, 'li li'))
        for j in range(1, x+1):
            a1 = driver.find_element(By.XPATH,
                                     f'/html/body/div/div/div/table/tbody/tr/td[1]/div[3]/ul/li[{i}]/ul/li[{j}]/a/span').click()
        driver.find_element(By.TAG_NAME, 'h1').text
