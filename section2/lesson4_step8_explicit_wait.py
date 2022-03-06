from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import math


def calc(x: str) -> str:
    return str(math.log(abs(12*math.sin(int(x)))))


def chrome_driver_manager() -> webdriver.Chrome:
    """Попытка подключить менеджер для автоматизации управления драйверами,
    в случае его отсутствия запускает драйвер установленный в системе"""
    try:
        from webdriver_manager.chrome import ChromeDriverManager
    except ModuleNotFoundError:
        return webdriver.Chrome(
            executable_path=r'..\venv\bin\chromedriver.exe')
    return webdriver.Chrome(ChromeDriverManager().install())


def main():
    link = "https://suninjuly.github.io/explicit_wait2.html"
    try:
        browser = chrome_driver_manager()
        browser.get(link)
        WebDriverWait(browser, 12).until(
            ec.text_to_be_present_in_element((By.ID, "price"), '$100')
        )
        browser.find_element_by_id("book").click()
        x_element = browser.find_element_by_id('input_value')
        x = x_element.text
        browser.find_element_by_id('answer').send_keys(calc(x))
        button = WebDriverWait(browser, 5).until(
            ec.element_to_be_clickable((By.ID, "solve"))
        )
        button.click()
    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == '__main__':
    main()
