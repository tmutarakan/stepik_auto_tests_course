from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

try:
    # link = "http://suninjuly.github.io/registration1.html"
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(link)

    input1 = browser.find_element_by_xpath('//input[@placeholder="Input your first name"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath('//input[@placeholder="Input your last name"]')
    input2.send_keys("Petrovsky")
    input3 = browser.find_element_by_xpath('//input[@placeholder="Input your email"]')
    input3.send_keys("Smolensk@email.sm")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")

    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:

    time.sleep(10)

    browser.quit()