import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://localhost/litecart/en/")
    m = len(driver.find_elements(By.XPATH, '//*[@id="box-most-popular"]/div/ul/li'))
    m1 = len(driver.find_elements(By.XPATH, '//*[@id="box-latest-products"]/div/ul/li'))
    
    for i in range(1, m+1):
        assert len(driver.find_elements(By.XPATH, f'//*[@id="box-most-popular"]/div/ul/li[{i}]/a[1]/div[1]/div'))==1, "More then 1 time"

    for j in range(1, m1 + 1):
        assert len(driver.find_elements(By.XPATH, f'//*[@id="box-latest-products"]/div/ul/li[{j}]/a[1]/div[1]/div'))==1, "More then 1 time"






        



