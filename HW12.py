import os
import pytest
from selenium import webdriver
import time
from random import randint



@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    time.sleep(10)
    driver.get("http://localhost/litecart/admin/?category_id=0&app=catalog&doc=edit_product")
    list = []

    ###General tab
    driver.find_element_by_css_selector("#tab-general > table > tbody > tr:nth-child(1) > td > label:nth-child(3) > input[type=radio]").click()
    driver.find_element_by_xpath("/html/body/div[2]/div/div/table/tbody/tr/td[3]/form/div/div/div[1]/table/tbody/tr[1]/td/label[1]/input")
    driver.find_element_by_name("name[en]").send_keys("Gold Duck8")
    driver.find_element_by_name("code").send_keys("11118")
    driver.find_element_by_css_selector("#tab-general > table > tbody > tr:nth-child(4) > td > div > table > tbody > tr:nth-child(1) > td:nth-child(1) > input[type=checkbox]").click()
    driver.find_element_by_css_selector("#tab-general > table > tbody > tr:nth-child(4) > td > div > table > tbody > tr:nth-child(2) > td:nth-child(1) > input[type=checkbox]").click()
    driver.find_element_by_name("product_groups[]").click()
    driver.find_element_by_name("quantity").send_keys("10000")
    driver.find_element_by_name("new_images[]").send_keys(os.getcwd() + "\duck.jpg")
    driver.find_element_by_name("date_valid_from").send_keys("20122022")
    driver.find_element_by_name("date_valid_to").send_keys("20122023")
    time.sleep(10)

    ### Information tab
    driver.find_element_by_xpath("/html/body/div[2]/div/div/table/tbody/tr/td[3]/form/div/ul/li[2]/a").click()
    time.sleep(10)
    driver.find_element_by_xpath("/html/body/div[2]/div/div/table/tbody/tr/td[3]/form/div/div/div[2]/table/tbody/tr[1]/td/select/option[2]").click()
    driver.find_element_by_name("keywords").send_keys("Duck")
    driver.find_element_by_name("short_description[en]").send_keys("short_description")
    driver.find_element_by_css_selector("div.trumbowyg-editor").send_keys("Description")
    driver.find_element_by_name("head_title[en]").send_keys("Title")
    driver.find_element_by_name("meta_description[en]").send_keys("Meta_data")
    driver.find_element_by_xpath("/html/body/div[2]/div/div/table/tbody/tr/td[3]/form/div/ul/li[4]/a").click()
    time.sleep(10)

    ###Prices
    driver.find_element_by_name("purchase_price").send_keys("20")
    driver.find_element_by_css_selector("#tab-prices > table:nth-child(2) > tbody > tr > td > select > option:nth-child(2)").click()
    driver.find_element_by_name("prices[USD]").send_keys("20")
    driver.find_element_by_name("prices[EUR]").send_keys("23")
    driver.find_element_by_name("save").click()
    time.sleep(10)

    ### check out the new Duck in Catalog
    m = len(driver.find_elements_by_css_selector("tr.row"))  # count of all elements
    for i in range(2, m + 2):
        ducks_name = driver.find_elements_by_css_selector(f'#content > form > table > tbody > tr:nth-child({i}) > td:nth-child(3) > a')
        for y in ducks_name:
            y = y.text
            if y == "Gold Duck8":
                print("The Gold Duck8 was added")
    time.sleep(10)






