import unittest
from selenium import webdriver


class TestAbs(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_abs1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")
        input1 = browser.find_element_by_css_selector('[class="first_block"] > [class="form-group first_class"] > [class="form-control first"]')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector('[class="first_block"] > [class="form-group second_class"] > [class="form-control second"]')
        input2.send_keys("Ivanovich")
        input3 = browser.find_element_by_css_selector('[class="first_block"] > [class="form-group third_class"] > [class="form-control third"]')
        input3.send_keys("proverka@yandex.ru")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Should be equal Test1")

    def test_abs2(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")
        input1 = browser.find_element_by_css_selector('[class="first_block"] > [class="form-group first_class"] > [class="form-control first"]')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector('[class="first_block"] > [class="form-group second_class"] > [class="form-control second"]')
        input2.send_keys("Ivanovich")
        input3 = browser.find_element_by_css_selector('[class="first_block"] > [class="form-group third_class"] > [class="form-control third"]')
        input3.send_keys("proverka@yandex.ru")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Should be equal Test2")


if __name__ == "__main__":
    unittest.main()
