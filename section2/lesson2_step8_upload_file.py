from selenium import webdriver
import time
import os


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
    link = "http://suninjuly.github.io/file_input.html"
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    try:
        browser = chrome_driver_manager()
        browser.get(link)
        input_first_name = browser.find_element_by_css_selector(
            '.form-control[name="firstname"]')
        input_first_name.send_keys("Ivan")
        input_last_name = browser.find_element_by_css_selector(
            '.form-control[name="lastname"]')
        input_last_name.send_keys("Petrov")
        input_email = browser.find_element_by_css_selector(
            '.form-control[name="email"]')
        input_email.send_keys("mail@mail.com")
        view = browser.find_element_by_id('file')
        view.send_keys(file_path)
        browser.find_element_by_css_selector('.btn.btn-primary').click()
    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == '__main__':
    main()
