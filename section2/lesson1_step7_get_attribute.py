from selenium import webdriver
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
    link = "http://suninjuly.github.io/get_attribute.html"
    try:
        browser = chrome_driver_manager()
        browser.get(link)
        x_element = browser.find_element_by_id('treasure')
        x = x_element.get_attribute("valuex")
        browser.find_element_by_id('answer').send_keys(calc(x))
        browser.find_element_by_id('robotCheckbox').click()
        browser.find_element_by_id('robotsRule').click()
        browser.find_element_by_css_selector('.btn.btn-default').click()
    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == '__main__':
    main()
