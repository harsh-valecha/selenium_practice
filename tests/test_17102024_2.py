from selenium import webdriver
from selenium.webdriver.common.by import By
# https://katalon-demo-cura.herokuapp.com/


def test_chrome_current_url():
    driver= webdriver.Chrome()
    driver.get('https://katalon-demo-cura.herokuapp.com/')
    make_appointment = driver.find_element(By.ID,'btn-make-appointment')
    make_appointment.click()

    assert driver.current_url == 'https://katalon-demo-cura.herokuapp.com/'
    driver.quit()



