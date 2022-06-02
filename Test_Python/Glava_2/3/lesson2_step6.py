from selenium import webdriver
import math
link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

browser.find_element_by_tag_name('.btn').click()
browser.switch_to.window(browser.window_handles[1])
x = browser.find_element_by_id("input_value").text
browser.find_element_by_id("answer").send_keys(str(math.log(abs(12 * math.sin(int(x))))))
browser.find_element_by_tag_name('.btn').click()
