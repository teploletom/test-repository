from selenium.webdriver.support.color import Color

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
    #main page
    driver.get("http://localhost/litecart/en/")
    name_m = driver.find_element_by_css_selector("#box-campaigns > div > ul > li > a.link > div.name").text
    regular_price_m = driver.find_element_by_css_selector("#box-campaigns > div > ul > li > a.link > div.price-wrapper > s").text
    sale_price_m = driver.find_element_by_css_selector("#box-campaigns > div > ul > li > a.link > div.price-wrapper > strong").text

    gray_col_m = driver.find_element_by_css_selector("#box-campaigns > div > ul > li > a.link > div.price-wrapper > s").value_of_css_property("color") #R = G = B
    driver.find_element_by_css_selector("#box-campaigns > div > ul > li > a.link > div.price-wrapper > s").value_of_css_property("text-decoration")
    red_col_m = driver.find_element_by_css_selector("#box-campaigns > div > ul > li > a.link > div.price-wrapper > strong").value_of_css_property("color") # G = B = 0
    driver.find_element_by_css_selector("#box-campaigns > div > ul > li > a.link > div.price-wrapper > strong").value_of_css_property("font-weight")
    size_reg_m = driver.find_element_by_css_selector(
        "#box-campaigns > div > ul > li > a.link > div.price-wrapper > s").value_of_css_property("font-size")
    size_sale_m = driver.find_element_by_css_selector(
        "#box-campaigns > div > ul > li > a.link > div.price-wrapper > strong").value_of_css_property("font-size")

    # color main page
    converted_gray_col_m = Color.from_string(gray_col_m).rgba  # converted for all browsers
    converted_red_col_m = Color.from_string(red_col_m).rgba  # converted for all browsers

    converted_gray_col_m_list = converted_gray_col_m.split()
    assert converted_gray_col_m_list[0] == 'rgba(119,' and converted_gray_col_m_list[1] == '119,' and converted_gray_col_m_list[2] == '119,', "color is not grey"

    converted_red_col_m_list = converted_red_col_m.split()
    assert converted_red_col_m_list[1] == '0,' and converted_red_col_m_list[2] == '0,', "Color is not red"

    #goods page
    driver.find_element_by_css_selector("#box-campaigns > div > ul > li > a.link").click()
    name_g = driver.find_element_by_css_selector("h1.title").text
    regular_price_g = driver.find_element_by_css_selector("s.regular-price").text
    sale_price_g = driver.find_element_by_css_selector("strong.campaign-price").text

    gray_col_g = driver.find_element_by_css_selector("s.regular-price").value_of_css_property("color") #R = G = B
    driver.find_element_by_css_selector("s.regular-price").value_of_css_property("text-decoration")
    red_col_g = driver.find_element_by_css_selector("strong.campaign-price").value_of_css_property("color") # G = B = 0

    driver.find_element_by_css_selector("strong.campaign-price").value_of_css_property("font-weight")
    size_reg_g = driver.find_element_by_css_selector("s.regular-price").value_of_css_property("font-size")
    size_sale_g = driver.find_element_by_css_selector("strong.campaign-price").value_of_css_property("font-size")

    #color goods page
    converted_gray_col_g = Color.from_string(gray_col_g).rgba # converted for all browsers
    converted_red_col_g = Color.from_string(red_col_g).rgba # converted for all browsers

    converted_gray_col_g_list = converted_gray_col_g.split()
    assert converted_gray_col_g_list[0] == 'rgba(102,' and converted_gray_col_g_list[1] == '102,' and converted_gray_col_g_list[2] == '102,', "color is not grey"

    converted_red_col_g_list = converted_red_col_g.split()
    assert converted_red_col_g_list[1] == '0,' and converted_red_col_g_list[2] == '0,', "Color is not red"

    #checks
    assert name_m == name_g, "Not equal"
    assert regular_price_m == regular_price_g, "Not equal"
    assert sale_price_m == sale_price_g, "Not equal"
    assert size_reg_m < size_sale_m, "Size regular is bigger of size sale on the main page"
    assert size_reg_g < size_sale_g, "Size regular is bigger of size sale on the goods page"








