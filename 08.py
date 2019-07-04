from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)
button = browser.find_element_by_css_selector("button.btn")
x = browser.find_element_by_id('input_value').text
y = calc(x)
answer = browser.find_element_by_id('answer')   
answer.send_keys(y)
ch = browser.find_element_by_id('robotCheckbox')
ch.click()
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
ch2 = browser.find_element_by_id('robotsRule')
ch2.click()


browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()