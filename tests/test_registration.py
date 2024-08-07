import locators
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def test_success_registration(create_email, create_correct_password, create_username):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, locators.login_to_account_button).click()
    driver.find_element(By.XPATH, locators.go_to_registration_button).click()
    driver.find_element(By.XPATH, locators.username).send_keys(create_username)
    driver.find_element(By.XPATH, locators.email).send_keys(create_email)
    driver.find_element(By.XPATH, locators.password).send_keys(create_correct_password)
    driver.find_element(By.XPATH, locators.register).click()
    WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, locators.header_login)))
    assert driver.find_element(By.XPATH, locators.header_login)
    driver.quit()


def test_incorrect_password_error(create_email, create_incorrect_password, create_username):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, locators.login_to_account_button).click()
    driver.find_element(By.XPATH, locators.go_to_registration_button).click()
    driver.find_element(By.XPATH, locators.username).send_keys(create_username)
    driver.find_element(By.XPATH, locators.email).send_keys(create_email)
    driver.find_element(By.XPATH, locators.password).send_keys(create_incorrect_password)
    driver.find_element(By.XPATH, locators.register).click()
    WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, locators.incorrect_password_error)))
    assert driver.find_element(By.XPATH, locators.incorrect_password_error)
    driver.quit()

