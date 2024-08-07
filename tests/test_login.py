import locators
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def test_login_through_login_to_account_button():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, locators.login_to_account_button).click()
    driver.find_element(By.XPATH, locators.email).send_keys('alena_podgornaia_1245@yandex.ru')
    driver.find_element(By.XPATH, locators.password).send_keys('123456')
    driver.find_element(By.XPATH, locators.login_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, locators.create_order)))
    assert driver.find_element(By.XPATH, locators.create_order)
    driver.quit()


def test_login_through_personal_account_button():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, locators.personal_account_button).click()
    driver.find_element(By.XPATH, locators.email).send_keys('alena_podgornaia_1245@yandex.ru')
    driver.find_element(By.XPATH, locators.password).send_keys('123456')
    driver.find_element(By.XPATH, locators.login_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, locators.create_order)))
    assert driver.find_element(By.XPATH, locators.create_order)
    driver.quit()


def test_login_through_login_button_on_registration_page():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(By.XPATH, locators.to_login_form).click()
    driver.find_element(By.XPATH, locators.email).send_keys('alena_podgornaia_1245@yandex.ru')
    driver.find_element(By.XPATH, locators.password).send_keys('123456')
    driver.find_element(By.XPATH, locators.login_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, locators.create_order)))
    assert driver.find_element(By.XPATH, locators.create_order)
    driver.quit()


def test_login_through_reset_password_form():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
    driver.find_element(By.XPATH, locators.to_login_form).click()
    driver.find_element(By.XPATH, locators.email).send_keys('alena_podgornaia_1245@yandex.ru')
    driver.find_element(By.XPATH, locators.password).send_keys('123456')
    driver.find_element(By.XPATH, locators.login_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, locators.create_order)))
    assert driver.find_element(By.XPATH, locators.create_order)
    driver.quit()
