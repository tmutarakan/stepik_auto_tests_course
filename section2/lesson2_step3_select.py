from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


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
    link = "http://suninjuly.github.io/selects1.html"
    try:
        browser = chrome_driver_manager()
        browser.get(link)
        num1 = browser.find_element_by_id('num1')
        num1 = int(num1.text)
        num2 = browser.find_element_by_id('num2')
        num2 = int(num2.text)
        select = Select(browser.find_element_by_tag_name("select"))
        select.select_by_value(str(num1+num2))
        browser.find_element_by_css_selector('.btn.btn-default').click()
    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == '__main__':
    main()
