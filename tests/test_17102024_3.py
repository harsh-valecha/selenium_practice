from selenium import webdriver
from selenium.webdriver.common.by import By


def test_make_appointment():
    driver = webdriver.Chrome()
    driver.get('https://katalon-demo-cura.herokuapp.com/')
    make_appointment = driver.find_element(By.ID, 'btn-make-appointment')
    make_appointment.click()
    username = driver.find_element(By.ID,'txt-username')
    username.send_keys('John Doe')
    password = driver.find_element(By.ID,'txt-password')
    password.send_keys('ThisIsNotAPassword')
    login = driver.find_element(By.ID,'btn-login')
    login.click()
    assert driver.current_url =='https://katalon-demo-cura.herokuapp.com/#appointment'
