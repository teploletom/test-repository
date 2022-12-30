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

    product_count = driver.find_elements_by_css_selector('li.product')
    for i in product_count:
        assert len(i.find_elements_by_css_selector('div.sticker')) == 1, "More/less then one"





        



