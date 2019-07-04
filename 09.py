from selenium import webdriver
link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)
n = browser.find_element_by_name('firstname')
n.send_keys('1')
s = browser.find_element_by_name('lastname')
s.send_keys('1')
e = browser.find_element_by_name('email')
e.send_keys('1')
f = browser.find_element_by_name('file')
f.send_keys('e://01.txt')
button = browser.find_element_by_css_selector("button.btn")
button.click()
