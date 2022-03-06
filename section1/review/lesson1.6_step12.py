from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    # link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(link)

    # fill required fields
    first_name = browser.find_element_by_css_selector("input[placeholder=\"Input your first name\"].first.form-control")
    first_name.send_keys("Ivan")
    second_name = browser.find_element_by_css_selector("input[placeholder=\"Input your last name\"].second.form-control")
    second_name.send_keys("Petrov")
    email = browser.find_element_by_css_selector("input[placeholder=\"Input your email\"].third.form-control")
    email.send_keys("ipetr@mail.ru")

    # send filled form
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


    # wait page loading in case of successful registration
    time.sleep(1)

    # find element with welcome text
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    # check welcome text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()