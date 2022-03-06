from selenium import webdriver
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
    link = "http://suninjuly.github.io/cats.html"
    try:
        browser = chrome_driver_manager()
        browser.get(link)
        browser.find_element_by_id("button")
    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == '__main__':
    main()
