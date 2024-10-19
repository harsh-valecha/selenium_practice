from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

# <input type="email" class="text-input W(100%)" name="username" id="login-username" data-qa="hocewoqisi">
# <input type="password" class="text-input W(100%)" name="password" id="login-password" data-qa="jobodapuxe">
# <button type="submit" id="js-login-btn" class="btn btn--positive btn--inverted W(100%) H(48px) Fz(16px)" onclick="login.login(event)" data-qa="sibequkica">
# 									<span class="icon loader hidden" data-qa="zuyezasugu"></span>
# 									<span data-qa="ezazsuguuy">Sign in</span>
# 								</button>
# <div class="notification-box-description" id="js-notification-box-msg" data-qa="rixawilomi">Your email, password, IP address or location did not match</div>



@pytest.mark.src19test1
def test_verify_invalid_login():
    driver = webdriver.Chrome()
    driver.get('https://app.vwo.com/#/login')

    # finding element by id
    username = driver.find_element(By.ID,'login-username')
    username.send_keys('test@gmail.com')

    # finding element by name
    password = driver.find_element(By.NAME,'password')
    password.send_keys('passo1234')

    login = driver.find_element(By.ID,'js-login-btn')
    login.click()

    alert= driver.find_element(By.CLASS_NAME,'notification-box-description')
    assert alert.text=='Your email, password, IP address or location did not match'

    driver.close()


@pytest.mark.src19test2
def test_invalid_email_free_trial():
    driver = webdriver.Chrome()
    driver.get('https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage')

    # finding element by xpath
    email = driver.find_element(By.XPATH,'//*[@id="page-v1-step1-email"]')
    email.send_keys('testhola')

    # check
    tick = driver.find_element(By.CSS_SELECTOR,'#page-589cu-gdpr-consent-checkbox')
    tick.click()

    driver.close()