from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait


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
    driver.find_element_by_css_selector("#content > div > a").click()  # button new country

    main_window = driver.current_window_handle
    links = driver.find_elements_by_css_selector("i.fa.fa-external-link")
    for y in links:
        y.click()
        wait = WebDriverWait(driver, 15)  # wait the new window
        wait.until(EC.number_of_windows_to_be(2))
        # Wait till new window fully loaded
   #     WebDriverWait(driver, 15).until(EC.url_changes("about:blank"))

        # Switch to second window
        new_window = driver.window_handles[1]
        driver.switch_to.window(new_window)
        driver.close()
        # Switch to main window
        driver.switch_to.window(main_window)

