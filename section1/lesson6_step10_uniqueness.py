from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input_first_name = browser.find_element_by_css_selector(
        'input[placeholder="Input your first name"]'
    )
    input_first_name.send_keys("Ivan")

    input_last_name = browser.find_element_by_css_selector(
        'input[placeholder="Input your last name"]'
    )
    input_last_name.send_keys("Petrov")

    input_email = browser.find_element_by_css_selector(
        'input[placeholder="Input your email"]'
    )
    input_email.send_keys("mail@mail.com")

    input_phone = browser.find_element_by_css_selector(
        'input[placeholder="Input your phone:"]'
    )
    input_phone.send_keys("+00000000000")

    input_address = browser.find_element_by_css_selector(
        'input[placeholder="Input your address:"]'
    )
    input_address.send_keys("nowhere")

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
