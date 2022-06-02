from selenium import webdriver
import math
from selenium.webdriver.support.ui import Select
link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_css_selector('[id="input_value"]').text
option1 = str(math.log(abs(12 * math.sin(int(input1)))))
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
input2 = browser.find_element_by_css_selector('[id="answer"]')
input2.send_keys(option1)
browser.find_element_by_css_selector('[type="checkbox"]').click()
browser.find_element_by_css_selector('[id="robotsRule"]').click()
button = browser.find_element_by_tag_name(".btn").click()