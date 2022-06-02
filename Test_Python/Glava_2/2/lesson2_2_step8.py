import os
from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

browser.find_element_by_css_selector('[name="firstname"]').send_keys('Artem')
browser.find_element_by_css_selector('[name="lastname"]').send_keys('Lastnovich')
browser.find_element_by_css_selector('[name="email"]').send_keys('ya@ya.ru')

current_dir = os.path.abspath(os.path.dirname(__file__))
with open('something.txt', 'w') as file:
    file.write('Ofigeti vot bi naychitsya')
file_name = "something.txt"
file_path = os.path.join(current_dir, file_name)
element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
element.send_keys(file_path)
browser.find_element_by_tag_name(".btn").click()