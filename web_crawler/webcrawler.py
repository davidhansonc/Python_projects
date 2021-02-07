# -*- coding: utf-8 -*-
# @Author: davidhansonc
# @Date:   2021-01-21 09:58:35
# @Last Modified by:   davidhansonc
# @Last Modified time: 2021-01-21 13:12:11
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
assert "Selenium" in driver.title

textbox = driver.find_element_by_css_selector('input#user-message.form-control')
textbox.clear()
textbox.send_keys("my message")
time.sleep(0.5)

if driver.find_element_by_css_selector('a#at-cv-lightbox-close.at4-close'):
    dialogue_close = driver.find_element_by_css_selector('a#at-cv-lightbox-close.at4-close')
    dialogue_close.click()
    time.sleep(0.5)

button = driver.find_element_by_css_selector('button.btn.btn-default')
button.click()
time.sleep(0.5)

output_message = driver.find_element_by_css_selector('span#display')
assert "my message" in output_message.text


textbox2 = driver.find_element_by_css_selector('input#sum1.form-control')
textbox3 = driver.find_element_by_css_selector('input#sum2.form-control')
textbox2.clear()
textbox3.clear()
textbox2.send_keys("3")
textbox3.send_keys("4")
time.sleep(0.5)

button = driver.find_elements_by_css_selector('button.btn.btn-default')[1]
button.click()


time.sleep(2)
driver.quit()
