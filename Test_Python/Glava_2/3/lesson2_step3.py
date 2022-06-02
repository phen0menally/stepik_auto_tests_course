
from selenium import webdriver
import math


link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

browser.find_element_by_tag_name(".btn").click()
alert = browser.switch_to.alert
alert.accept()
x = browser.find_element_by_id("input_value").text
formula = str(math.log(abs(12 * math.sin(int(x)))))
browser.find_element_by_id("answer").send_keys(formula)
browser.find_element_by_tag_name('.btn').click()