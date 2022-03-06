import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get('http://suninjuly.github.io/registration2.html')
    
    input1 = browser.find_element(By.CSS_SELECTOR, "input.form-control.first[required]")
    input1.send_keys('Ivan')
    
    input2 = browser.find_element(By.CSS_SELECTOR, "input.form-control.second[required]")
    input2.send_keys('Ivanov')

    input3 = browser.find_element(By.CSS_SELECTOR, "input.form-control.third[required]")
    input3.send_keys('dsgdfbigd@sdfsfd.re')

    time.sleep(2)
    
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

    time.sleep(1)
    
    welcome_text_elt = browser.find_element(By.TAG_NAME, 'h1')
    welcome_text = welcome_text_elt.text
    
    assert 'Congratulations! You have successfully registered!' == welcome_text

finally:
    time.sleep(5)
    browser.quit()
    print('Test 1: OK!')
