﻿from selenium import webdriver
link = "http://suninjuly.github.io/find_xpath_form"
browser = webdriver.Chrome()
browser.get(link)
input1 = browser.find_element_by_tag_name('input')
input1.send_keys("1")
input2 = browser.find_element_by_name("last_name")
input2.send_keys("1")
input3 = browser.find_element_by_class_name('city')
input3.send_keys("1")
input4 = browser.find_element_by_id("country")
input4.send_keys("1")
button = browser.find_element_by_xpath("//button[text()='Отправить']")
button.click()