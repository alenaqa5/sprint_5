import locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest
import credentials


@pytest.mark.parametrize('setup', ['main_page'], indirect=True)
def test_login_through_login_to_account_button(setup):
    driver = setup
    driver.find_element(By.XPATH, locators.login_to_account_button).click()
    driver.find_element(By.XPATH, locators.email).send_keys(credentials.email)
    driver.find_element(By.XPATH, locators.password).send_keys(credentials.password)
    driver.find_element(By.XPATH, locators.login_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, locators.create_order)))
    assert driver.find_element(By.XPATH, locators.create_order)


@pytest.mark.parametrize('setup', ['main_page'], indirect=True)
def test_login_through_personal_account_button(setup):
    driver = setup
    driver.find_element(By.XPATH, locators.personal_account_button).click()
    driver.find_element(By.XPATH, locators.email).send_keys(credentials.email)
    driver.find_element(By.XPATH, locators.password).send_keys(credentials.password)
    driver.find_element(By.XPATH, locators.login_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, locators.create_order)))
    assert driver.find_element(By.XPATH, locators.create_order)


@pytest.mark.parametrize('setup', ['registration'], indirect=True)
def test_login_through_login_button_on_registration_page(setup):
    driver = setup
    driver.find_element(By.XPATH, locators.to_login_form).click()
    driver.find_element(By.XPATH, locators.email).send_keys(credentials.email)
    driver.find_element(By.XPATH, locators.password).send_keys(credentials.password)
    driver.find_element(By.XPATH, locators.login_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, locators.create_order)))
    assert driver.find_element(By.XPATH, locators.create_order)


@pytest.mark.parametrize('setup', ['reset_password'], indirect=True)
def test_login_through_reset_password_form(setup):
    driver = setup
    driver.find_element(By.XPATH, locators.to_login_form).click()
    driver.find_element(By.XPATH, locators.email).send_keys(credentials.email)
    driver.find_element(By.XPATH, locators.password).send_keys(credentials.password)
    driver.find_element(By.XPATH, locators.login_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, locators.create_order)))
    assert driver.find_element(By.XPATH, locators.create_order)
