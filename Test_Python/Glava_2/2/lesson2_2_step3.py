import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_css_selector('[id="num1"]').text
input2 = browser.find_element_by_css_selector('[id="num2"]').text
select = Select(browser.find_element_by_css_selector('[id="dropdown"]'))
summa = int(input1)+int(input2)
select.select_by_value(str(summa))
button = browser.find_element_by_css_selector("[type=submit]")
button.click()