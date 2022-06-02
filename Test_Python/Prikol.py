from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://yandex.ru/"
browser = webdriver.Chrome()
browser.get(link)

browser.find_element(By.ID, "text").send_keys("Ozon")
browser.find_element_by_css_selector('[type="submit"]').click()
browser.find_element_by_partial_link_text(" — интернет-магазин. Миллионы товаров по...").click()

#data = input('Введи наименование товара ')
# time.sleep(2)
# browser.find_element_by_css_selector('[placeholder="Искать на Ozon"]').send_keys("мыло")
# browser.find_element_by_css_selector('[type="submit"]')
quit()

