from selenium.webdriver.support.color import Color

import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    #main page
    driver.get("http://localhost/litecart/en/")
    name_m = driver.find_element_by_css_selector("#box-campaigns div.name").text
    regular_price_m = driver.find_element_by_css_selector("#box-campaigns div.price-wrapper > s").text
    regular_price_m = float(regular_price_m[1:])
    sale_price_m = driver.find_element_by_css_selector("#box-campaigns div.price-wrapper > strong").text
    sale_price_m = float(sale_price_m[1:])

    gray_col_m = driver.find_element_by_css_selector("#box-campaigns div.price-wrapper > s").value_of_css_property("color") #R = G = B
    text_decoration_m = driver.find_element_by_css_selector("#box-campaigns div.price-wrapper > s").value_of_css_property("text-decoration")
    text_decoration_m = text_decoration_m[:12]
    red_col_m = driver.find_element_by_css_selector("#box-campaigns div.price-wrapper > strong").value_of_css_property("color") # G = B = 0
    font_weight_m = driver.find_element_by_css_selector("#box-campaigns div.price-wrapper > strong").value_of_css_property("font-weight")
    size_reg_m = driver.find_element_by_css_selector("#box-campaigns div.price-wrapper > s").value_of_css_property("font-size")
    size_sale_m = driver.find_element_by_css_selector("#box-campaigns div.price-wrapper > strong").value_of_css_property("font-size")
    size_reg_m = float(size_reg_m[:-2])
    size_sale_m = float(size_sale_m[:-2])

    # color main page
    converted_gray_col_m = Color.from_string(gray_col_m).rgba  # converted for all browsers
    converted_red_col_m = Color.from_string(red_col_m).rgba  # converted for all browsers

    converted_gray_col_m_list = converted_gray_col_m.split()
    converted_gray_col_m_list[0] = converted_gray_col_m_list[0][5:]
    assert converted_gray_col_m_list[0] == converted_gray_col_m_list[1] == converted_gray_col_m_list[2], "color is not grey"

    converted_red_col_m_list = converted_red_col_m.split()
    assert converted_red_col_m_list[1] == '0,' and converted_red_col_m_list[2] == '0,', "Color is not red"

    #goods page
    driver.find_element_by_css_selector("#box-campaigns > div > ul > li > a.link").click()
    name_g = driver.find_element_by_css_selector("h1.title").text
    regular_price_g = driver.find_element_by_css_selector("s.regular-price").text
    regular_price_g = float(regular_price_g[1:])
    sale_price_g = driver.find_element_by_css_selector("strong.campaign-price").text
    sale_price_g = float(sale_price_g[1:])

    gray_col_g = driver.find_element_by_css_selector("s.regular-price").value_of_css_property("color") #R = G = B
    text_decoration_g = driver.find_element_by_css_selector("s.regular-price").value_of_css_property("text-decoration")
    red_col_g = driver.find_element_by_css_selector("strong.campaign-price").value_of_css_property("color") # G = B = 0
    text_decoration_g = text_decoration_g[:12]

    font_weight_g = driver.find_element_by_css_selector("strong.campaign-price").value_of_css_property("font-weight")
    size_reg_g = driver.find_element_by_css_selector("s.regular-price").value_of_css_property("font-size")
    size_sale_g = driver.find_element_by_css_selector("strong.campaign-price").value_of_css_property("font-size")
    size_reg_g = float(size_reg_g[:-2])
    size_sale_g = float(size_sale_g[:-2])

    #color goods page
    converted_gray_col_g = Color.from_string(gray_col_g).rgba # converted for all browsers
    converted_red_col_g = Color.from_string(red_col_g).rgba # converted for all browsers

    converted_gray_col_g_list = converted_gray_col_g.split()
    converted_gray_col_g_list[0] = converted_gray_col_g_list[0][5:]
    assert converted_gray_col_g_list[0] == converted_gray_col_g_list[1] == converted_gray_col_g_list[2], "color is not grey"

    converted_red_col_g_list = converted_red_col_g.split()
    assert converted_red_col_g_list[1] == '0,' and converted_red_col_g_list[2] == '0,', "Color is not red"

    #checks
    assert name_m == name_g, "Not equal"

    assert regular_price_m == regular_price_g, "Not equal"
    assert sale_price_m == sale_price_g, "Not equal"

    assert size_reg_m < size_sale_m, "Size regular is bigger of size sale on the main page"
    assert size_reg_g < size_sale_g, "Size regular is bigger of size sale on the goods page"

    assert text_decoration_g == text_decoration_m == "line-through", "Line is not line-through"
    assert font_weight_g == font_weight_m == "700"

