import math
import time

from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    chest = browser.find_element_by_css_selector('#treasure')
    val = chest.get_attribute("valuex")
    browser.find_element_by_id("answer").send_keys(calc(val))

    for selector in ['#robotCheckbox', '#robotsRule', '.btn']:
        browser.find_element_by_css_selector(selector).click()

finally:
    time.sleep(6)

    browser.quit()
