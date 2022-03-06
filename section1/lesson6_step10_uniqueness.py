from selenium import webdriver
import time


def chrome_driver_manager() -> webdriver.Chrome:
    """Попытка подключить менеджер для автоматизации управления драйверами,
    в случае его отсутствия запускает драйвер установленный в системе"""
    try:
        from webdriver_manager.chrome import ChromeDriverManager
    except ModuleNotFoundError:
        return webdriver.Chrome()
    return webdriver.Chrome(ChromeDriverManager().install())


def main():
    link = "http://suninjuly.github.io/registration2.html"
    try:        
        browser = chrome_driver_manager()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input_first_name = browser.find_element_by_css_selector(
            '.first_block .first'
        )
        input_first_name.send_keys("Ivan")

        input_last_name = browser.find_element_by_css_selector(
            '.first_block .second'
        )
        input_last_name.send_keys("Petrov")

        input_email = browser.find_element_by_css_selector(
            '.first_block .third'
        )
        input_email.send_keys("mail@mail.com")

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
 
 
if __name__ == '__main__':
    main()
