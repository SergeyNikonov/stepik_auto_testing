from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
import os 
link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element_by_css_selector("button.btn")
button.click()

alert = browser.switch_to.alert
alert.accept()

x = browser.find_element_by_id('input_value').text
y = calc(x)
answer = browser.find_element_by_id('answer')   
answer.send_keys(y)

answer = browser.find_element_by_id('answer')   
answer.send_keys(y)
button = browser.find_element_by_css_selector("button.btn")
button.click()