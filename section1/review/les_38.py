from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(link)

    text_name = browser.find_element_by_css_selector('input[placeholder="Input your first name"]')
    text_name.send_keys('хуй')
    text_lastname = browser.find_element_by_css_selector('input[placeholder="Input your last name"]')
    text_lastname.send_keys('хуй')
    text_email = browser.find_element_by_css_selector('input[placeholder="Input your email"]')
    text_email.send_keys('хуй')


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()