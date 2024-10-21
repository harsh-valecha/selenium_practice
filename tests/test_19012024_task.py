from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_awesomeqa_registration():
    driver = webdriver.Chrome()
    driver.get('https://awesomeqa.com/ui/index.php?route=account/register')

    first_name = driver.find_element(By.CSS_SELECTOR,'#input-firstname')
    first_name.send_keys('Testhuoola')
    last_name = driver.find_element(By.CSS_SELECTOR,'#input-lastname')
    last_name.send_keys('Test')
    email = driver.find_element(By.CSS_SELECTOR,'#input-email')
    email.send_keys('testtimepass7@email.com')
    telephone = driver.find_element(By.CSS_SELECTOR,'#input-telephone')
    telephone.send_keys('686868686')
    password= driver.find_element(By.ID,'input-password')
    password.send_keys('password_is_good')
    confirm_password = driver.find_element(By.ID,'input-confirm')
    confirm_password.send_keys('password_is_good')
    subscribe_yes = driver.find_element(By.XPATH,"//input[@name='newsletter' and @value='1']")
    subscribe_yes.click()

    agree_checkbox = driver.find_element(By.XPATH,"//input[@name='agree']")
    agree_checkbox.click()
    continue_btn = driver.find_element(By.XPATH,"//input[@value='Continue']")
    continue_btn.click()

    assert driver.current_url =='https://awesomeqa.com/ui/index.php?route=account/success'
    # account_created = driver.find_element(By.TAG_NAME,'h1')
    # assert account_created.text =='Your Account Has Been Created!'
    driver.save_screenshot('screenshots/awesomeqa_resister.png')
    driver.close()


def test_vwo():
    driver = webdriver.Chrome()
    driver.get('https://app.vwo.com/#/login')

    username = driver.find_element(By.CSS_SELECTOR,'#login-username')
    username.send_keys('testuser')
    password = driver.find_element(By.CSS_SELECTOR,'#login-password')
    password.send_keys('testkarle')
    login_btn = driver.find_element(By.XPATH,"//button[@id='js-login-btn']")
    login_btn.click()

    wait = WebDriverWait(driver,10)
    msg = wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@class='notification-box-description']")))

    assert msg.text=='Your email, password, IP address or location did not match'
    driver.close()

